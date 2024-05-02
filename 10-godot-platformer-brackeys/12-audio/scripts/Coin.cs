using Godot;
using System;

public partial class Coin : Area2D
{
	// Called when the node enters the scene tree for the first time.
	public override void _Ready()
	{
		// on body entered
		Connect("body_entered", new Callable(this, nameof(OnBodyEntered)));		
	}

	// Called every frame. 'delta' is the elapsed time since the previous frame.
	public override void _Process(double delta)
	{
	}

	// on body entered
	private void OnBodyEntered(Node body)
	{
		// One way to collect coins using code:
		// if (body is Player){
		// 	var audio = GetNode<AudioStreamPlayer2D>("AudioStreamPlayer2D");
		// 	audio.Play();
		// 	Visible = false;
		// }

		// var audio = GetNode<AudioStreamPlayer2D>("AudioStreamPlayer2D");
		// audio.Play();
		var gameManager = GetNode<GameManager>("../../GameManager");
		gameManager.AddScore(1);
		//QueueFree();

		var animPlayer = GetNode<AnimationPlayer>("AnimationPlayer");
		animPlayer.Play("pickup");
	}

}
