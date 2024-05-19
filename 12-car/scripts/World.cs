using Godot;
using System;

public partial class World : Node3D
{
	// Called when the node enters the scene tree for the first time.
	public override void _Ready()
	{
		Input.MouseMode = Input.MouseModeEnum.Captured;
	}

	// Called every frame. 'delta' is the elapsed time since the previous frame.
	public override void _Process(double delta)
	{
	}

	public override void _Input(InputEvent @event)
	{
		// Check if the input event is pressing the "exit_game" action
		if (Input.IsActionPressed("exit_game"))
		{
			// Quit the game
			GetTree().Quit();
		}
	}
}
