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
	}
	
	private void OnResetTimerTimeout()
	{
		GetTree().ReloadCurrentScene();
	}

}
