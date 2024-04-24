using Godot;
using System;

public partial class Main : Node2D
{
	private Vector2 DINO_START_POS = new Vector2(150, 485);
	private Vector2 CAM_START_POS = new Vector2(576, 324);
	private Vector2 screen_size = new Vector2(0, 0);
	private int score = 0;
	public bool gameRunning = false;

	private float speed;
	private float START_SPEED = 200.0f;
	private float MAX_SPEED = 700.0f;
	// Called when the node enters the scene tree for the first time.
	// Reference to Dino
	private CharacterBody2D dino;
	private Camera2D camera;
	private ParallaxBackground bg;
	private StaticBody2D ground;
	public override void _Ready()
	{
		screen_size = GetViewport().GetVisibleRect().Size;
		dino = GetNode<Dino>("Dino");
		camera = GetNode<Camera2D>("Camera2D");
		bg = GetNode<ParallaxBackground>("Background");
		ground = GetNode<StaticBody2D>("Ground");
		NewGame();
	}

	public void NewGame(){
		score = 0;
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
		
			speed = START_SPEED * (float)delta;
			
			dino.Position += new Vector2(speed, 0);
			camera.Position += new Vector2(speed, 0);
			
			score += (int)speed;
			
			GD.Print(score);

			if (camera.Position.X - ground.Position.X  > screen_size.X * 1.5){
				ground.Position += new Vector2(screen_size.X, 0);
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
}
