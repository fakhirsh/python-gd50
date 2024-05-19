using Godot;
using System;

public partial class VehicleController : VehicleBody3D
{
	int engineForceFactor = 400;
	// Called when the node enters the scene tree for the first time.
	public override void _Ready()
	{
		
	}

	// Called every frame. 'delta' is the elapsed time since the previous frame.
	public override void _Process(double delta)
	{
		Steering = Input.GetAxis("move_right", "move_left") * 0.4f;
		EngineForce = Input.GetAxis("move_backward", "move_forward") * engineForceFactor;
	}
}
