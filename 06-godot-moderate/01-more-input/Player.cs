using Godot;
using System;

public partial class Player : Sprite2D
{
	// Called when the node enters the scene tree for the first time.
	public override void _Ready()
	{
	}

	// Called every frame. 'delta' is the elapsed time since the previous frame.
	public override void _Process(double delta)
	{
	}

	// input
	public override void _Input(InputEvent @event)
	{
		if (@event is InputEventMouseButton mouseEvent)
		{
			if (mouseEvent.Pressed)
			{
				GD.Print("Handled Mouse pressed at: " + mouseEvent.Position);
			}
		}
		
	}

	// Unhandled input
	public override void _UnhandledInput(InputEvent @event)
	{
		if (@event is InputEventKey eventKey)
		{
			if (eventKey.Pressed)
			{
				GD.Print("Key pressed: " + eventKey.Keycode);
			}
		}
		if (@event is InputEventMouseButton mouseEvent)
		{
			if (mouseEvent.Pressed)
			{
				GD.Print("Unhandled Mouse pressed at: " + mouseEvent.Position);
			}
		}
	}
}
