using Godot;
using System;

public partial class PlaneController : Node3D
{
	[Export] public float speed = 20.0f;
    [Export] public float rotationSpeed = 1.1f;
    [Export] public float cameraSmoothSpeed = 0.1f;
    
    private Camera3D camera;
    private Vector3 cameraOffset = new Vector3(0, 2, -5);
    
	// Called when the node enters the scene tree for the first time.
	public override void _Ready()
	{
		camera = GetNode<Camera3D>("Camera3D");
        //Input.MouseMode = Input.MouseModeEnum.Captured;
	}

	// Called every frame. 'delta' is the elapsed time since the previous frame.
	public override void _Process(double delta)
	{
		HandleMovement(delta);
	}

	private void HandleMovement(double delta)
    {
        if (Input.IsActionPressed("move_forward"))
        {
            Translate(Vector3.Forward * speed * (float)delta);
        }

        float yaw = 0.0f;
        float pitch = 0.0f;
        float roll = 0.0f;

        if (Input.IsActionPressed("yaw_right"))
        {
            yaw -= rotationSpeed;
        }

        if (Input.IsActionPressed("yaw_left"))
        {
            yaw += rotationSpeed;
        }

        if (Input.IsActionPressed("pitch_up"))
        {
            pitch -= rotationSpeed;
        }

        if (Input.IsActionPressed("pitch_down"))
        {
            pitch += rotationSpeed;
        }
		if (Input.IsActionPressed("roll_left"))
        {
            roll -= rotationSpeed;
        }
		if (Input.IsActionPressed("roll_right"))
        {
            roll += rotationSpeed;
        }

        RotateObjectLocal(Vector3.Up, (float)(yaw * delta));
        RotateObjectLocal(Vector3.Right, (float)(pitch * delta));
        RotateObjectLocal(Vector3.Forward, (float)(roll * delta));
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
