using Godot;
using System;
using System.Collections.Generic;

public partial class Main : Node2D
{
	// Called when the node enters the scene tree for the first time.
	private PackedScene blueBalloonScene; 
	private List<Balloon> balloons = new List<Balloon>();
	private Timer spawnTimer;
	int balloonHeight = 32;

	public int Score = 0;
	public int Lives = 5;

	public override void _Ready()
	{
		blueBalloonScene = GD.Load<PackedScene>("res://scenes/BlueBalloon.tscn");
		spawnTimer = GetNode<Timer>("SpawnTimer");
		spawnTimer.Connect("timeout", new Callable(this, nameof(OnSpawnTimerTimeout)));
		
	}

	public override void _Process(double delta)
	{
		foreach (Balloon balloon in balloons)
		{
			if (balloon.Position.Y + balloonHeight / 2 < 0)
			{
				balloon.remove = true;
				
				//////////////////
				// Remove a life:
				//
				// 
				//////////////////
			}
		}

		for (int i = balloons.Count - 1; i >= 0; i--)
		{
			if (balloons[i].remove)
			{
				balloons[i].QueueFree();
				balloons.RemoveAt(i);
			}
		}

		GD.Print("Score: ", Score, " --- " , "Balloons: ", balloons.Count, " --- " , "Lives: ", Lives);
		UodateLabels();
	}

	private void OnSpawnTimerTimeout()
	{
		Balloon blueBalloon = blueBalloonScene.Instantiate<Balloon>();
		blueBalloon.Position = new Vector2((float)GD.RandRange(0, GetViewportRect().Size.X), GetViewportRect().Size.Y + balloonHeight*2);
		AddChild(blueBalloon);
		balloons.Add(blueBalloon);
	}

	private void UodateLabels()
	{
		var canvas = GetNode<CanvasLayer>("HUD");

		canvas.GetNode<Label>("ScoreLbl").Text = "Score: " + Score;
		
		////////////////////////////////
		// Update time and Life labels:
		//
		//
		////////////////////////////////
		
	}
}
