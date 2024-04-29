using Godot;
using System;
using System.Collections.Generic;


public partial class Main : Node2D
{

	// preload each of the obstacle scenes
	private PackedScene barrel, bird, rock, stump;

	// add obstacles to the array
	private List<PackedScene> obstacleTypes = new List<PackedScene>();
    private List<Node2D> obstacles = new List<Node2D>();
	private int[] birdHeights = new int[] { 200, 390 };

	private Vector2 DINO_START_POS = new Vector2(150, 485);
	private Vector2 CAM_START_POS = new Vector2(576, 324);
	private Vector2 screen_size = new Vector2(0, 0);
	//ground height
	private int groundHeight;
	private int score = 0;
	public bool gameRunning = false;

	public float speed;
	private float START_SPEED = 350.0f;
	private float MAX_SPEED = 800.0f;
	private float SPEED_MODIFIER = 500.0f;
    private int difficulty;
    private const int MAX_DIFFICULTY = 2;

	// Called when the node enters the scene tree for the first time.
	// Reference to Dino
	private CharacterBody2D dino;
	private Camera2D camera;
	private ParallaxBackground bg;
	private StaticBody2D ground;

    private Node2D lastObs;
	private float minDistance = 300;  // Minimum distance from the right edge of the screen to generate new obstacles


	public override void _Ready()
	{

		barrel = GD.Load<PackedScene>("res://scenes/Barrel.tscn");
		bird = GD.Load<PackedScene>("res://scenes/Bird.tscn");
		rock = GD.Load<PackedScene>("res://scenes/Rock.tscn");
		stump = GD.Load<PackedScene>("res://scenes/Stump.tscn");

		screen_size = GetViewport().GetVisibleRect().Size;
		
		dino = GetNode<Dino>("Dino");
		camera = GetNode<Camera2D>("Camera2D");
		bg = GetNode<ParallaxBackground>("Background");
		ground = GetNode<StaticBody2D>("Ground");
		groundHeight = ((Sprite2D)ground.GetNode("Sprite2D")).Texture.GetHeight();

		obstacleTypes.Add(barrel);
		obstacleTypes.Add(rock);
		obstacleTypes.Add(stump);

		NewGame();
	}

	public void NewGame(){
		score = 0;
		difficulty = 0;
		ShowScore();
		dino.Position = DINO_START_POS;
		dino.Velocity = new Vector2(0, 0);
		camera.Position = CAM_START_POS;
		ground.Position = new Vector2(0, 0);
		var startLabel = GetNode<Label>("HUD/StartLabel");
		startLabel.Visible = true;
	}

	// Called every frame. 'delta' is the elapsed time since the previous frame.
	public override void _Process(double delta)
	{
		if (gameRunning){
		
			speed = (START_SPEED + score / SPEED_MODIFIER) * (float)delta;
			
			GenerateObs();
			dino.Position += new Vector2(speed, 0);
			camera.Position += new Vector2(speed, 0);
			
			score += (int)speed;

			if (camera.Position.X - ground.Position.X  > screen_size.X * 1.5){
				ground.Position += new Vector2(screen_size.X, 0);
			}
			
			 for (int i = 0; i < obstacles.Count; i++)
            {
                if (obstacles[i].Position.X < camera.Position.X - screen_size.X)
                {
                    RemoveObs(obstacles[i]);
                }
            }
		}
		else{
			if(Input.IsActionJustPressed("dino_jump")){
				gameRunning = true;
				var startLabel = GetNode<Label>("HUD/StartLabel");
				startLabel.Visible = false;
			}
		}

		ShowScore();
	}

	private void ShowScore(){
		var scoreLabel = GetNode<Label>("HUD/ScoreLabel");
		scoreLabel.Text = "SCORE: " + score.ToString();

		// var HighScoreLabel = GetNode<Label>("HUD/HighScoreLabel");
		// HighScoreLabel.Text = "High Score: " + score.ToString();

	}

	private void GenerateObs()
	{
		// Generate ground obstacles
		//   - if there are no obstacles
		if (obstacles.Count == 0  || lastObs.Position.X < camera.Position.X + screen_size.X - minDistance)
		{
			PackedScene obsType = obstacleTypes[(int)(GD.Randi() % obstacleTypes.Count)];

			Node2D obs = obsType.Instantiate<Node2D>();
			int obsHeight = ((Sprite2D)obs.GetNode("Sprite2D")).Texture.GetHeight();
			Vector2 obsScale = ((Sprite2D)obs.GetNode("Sprite2D")).Scale;

			// Calculate obstacle's X coordinate based on the camera's current position plus some offset
        int obsX = (int)(camera.Position.X + screen_size.X + minDistance + GD.Randi() % 300);
			int obsY = (int)(screen_size.Y - groundHeight - (obsHeight * obsScale.Y / 2) + 5);
			lastObs = obs;

			AddObs(obs, obsX, obsY);
		}

		// Additionally, random chance to spawn a bird
		// if (difficulty == MAX_DIFFICULTY)
		{
			if (GD.Randi() % 200 == 0)
			{
				// // Generate bird obstacles
				Node2D obs = bird.Instantiate<Node2D>();
				int obsX = (int)(camera.Position.X + screen_size.X + minDistance); // Adding 300 to ensure it spawns off the right edge of the screen
				int obsY = birdHeights[GD.Randi() % birdHeights.Length];
				AddObs(obs, obsX, obsY);
			}
		}
	}

	 private void AddObs(Node2D obs, float x, float y)
    {
        obs.Position = new Vector2(x, y);
        ((Area2D)obs).BodyEntered += HitObs;
        AddChild(obs);
        obstacles.Add(obs);
    }

    private void RemoveObs(Node2D obs)
    {
        obs.QueueFree();
        obstacles.Remove(obs);
		GD.Print(obs, "Removed");
    }

	private void HitObs(Node body)
    {
        if (body.Name == "Dino")
        {
            GameOver();
        }
    }

	private void GameOver()
	{
		gameRunning = false;
		// var gameOverLabel = GetNode<Label>("HUD/GameOverLabel");
		// gameOverLabel.Visible = true;
	}

}
