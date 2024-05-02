using Godot;
using System;

public partial class Killzone : Area2D
{
	// Called when the node enters the scene tree for the first time.
	public override void _Ready()
	{
		Connect("body_entered", new Callable(this, nameof(OnBodyEntered)));
	}

	// Called every frame. 'delta' is the elapsed time since the previous frame.
	public override void _Process(double delta)
	{
	}
	private void OnBodyEntered(Node body)
	{
		var resetTimer = GetNode<Timer>("Timer");
		resetTimer.Start();
		resetTimer.Connect("timeout", new Callable(this, nameof(OnResetTimerTimeout)));
		Engine.TimeScale = 0.5f;
		
		body.GetNode<CollisionShape2D>("CollisionShape2D").QueueFree();
		
	}
	
	private void OnResetTimerTimeout()
	{
		Engine.TimeScale = 1.0f;
		GetTree().ReloadCurrentScene();
	}

}
