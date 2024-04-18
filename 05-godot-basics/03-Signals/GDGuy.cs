using Godot;
using System;

public partial class GDGuy : Sprite2D
{
	// Called when the node enters the scene tree for the first time.
	public override void _Ready()
	{
		Timer timer = GetNode<Timer>("Clock");
		timer.WaitTime = 1.0f;
		// Corrected Connect call using a Callable
        timer.Connect("timeout", new Callable(this, nameof(OnClockTimeout)));
		timer.Start();
	}

	private void OnClockTimeout()
	{
		float randX = (float)GD.RandRange(0, GetViewportRect().Size.X);
		float randY = (float)GD.RandRange(0, GetViewportRect().Size.Y);
		Position = new Vector2(randX, randY);
	}

	// Called every frame. 'delta' is the elapsed time since the previous frame.
	public override void _Process(double delta)
	{
	}
}
