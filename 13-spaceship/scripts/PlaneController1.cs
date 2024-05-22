using Godot;
using System;

public partial class PlaneController1 : Node3D
{
	[Export] public float speed = 20.0f;
    //[Export] public float rotationSpeed = 0.1f;
    [Export] public float rollSpeed = 1.0f;  // Separate roll speed variable

    [Export] public float cameraSmoothSpeed = 0.1f;
    [Export] public float mouseSensitivity = 0.1f;

    private Camera3D camera;
    private Vector3 cameraOffset = new Vector3(0, 2, -5);
    private Vector2 mouseDelta;

	// Called when the node enters the scene tree for the first time.
	public override void _Ready()
	{
		camera = GetNode<Camera3D>("Camera3D");
        Input.MouseMode = Input.MouseModeEnum.Captured;
	}

	// Called every frame. 'delta' is the elapsed time since the previous frame.
	public override void _Process(double delta)
	{
		HandleMovement(delta);
        HandleMouseInput(delta);
        //UpdateCameraPosition(delta);
	}

	private void HandleMovement(double delta)
    {
        if (Input.IsActionPressed("move_forward"))
        {
            Translate(Vector3.Forward * speed * (float)delta);
        }

        float roll = 0.0f;
        if (Input.IsActionPressed("roll_left"))
        {
            roll -= rollSpeed;
        }
		if (Input.IsActionPressed("roll_right"))
        {
            roll += rollSpeed;
        }
        RotateObjectLocal(Vector3.Forward, (float)(roll * delta));
    }

    private void HandleMouseInput(double delta)
    {
        float yaw = -mouseDelta.X * mouseSensitivity;
        float pitch = -mouseDelta.Y * mouseSensitivity;

        // Apply yaw (rotation around the Y axis)
        RotateObjectLocal(Vector3.Up, yaw * (float)delta);
        // Apply pitch (rotation around the X axis)
        RotateObjectLocal(Vector3.Right, pitch * (float)delta);
    }

	public override void _Input(InputEvent @event)
	{
		// Check if the input event is pressing the "exit_game" action
		if (Input.IsActionPressed("exit_game"))
		{
			// Quit the game
			GetTree().Quit();
		}
        if (@event is InputEventMouseMotion mouseEvent)
        {
            mouseDelta = mouseEvent.Relative;
        }

        
	}

}
