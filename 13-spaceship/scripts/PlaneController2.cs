using Godot;
using System;

public partial class PlaneController2 : Node3D
{
	[Export] public float speed = 50.0f;
    //[Export] public float rotationSpeed = 0.1f;
    [Export] public float rollSpeed = 1.0f;  // Separate roll speed variable

    [Export] public float cameraSmoothSpeed = 5.0f; // Smoothness factor for camera movement
    [Export] public float cameraDistance = 10.0f; // Distance behind the ship
    [Export] public float fixedYDistance = 5.0f; // Fixed height above the ship
    [Export] public float mouseSensitivity = 0.1f;

    private Camera3D camera;
    private Vector3 cameraOffset = new Vector3(0, 2, -5);
    private Vector2 mouseDelta;
    [Export] public PackedScene bulletScene;

    [Export] public float fireRate = 10.0f; // Bullets per second
    private bool isFiring = false;
    private float timeSinceLastShot = 0.0f;
    private float currentRoll = 0.0f;
    private float targetRoll = 0.0f;
	// Called when the node enters the scene tree for the first time.

    [Export] public float maxSpeed = 100.0f; // Maximum forward speed
    [Export] public float acceleration = 1.0f; // Acceleration rate
    private float currentSpeed = 0.0f;

	public override void _Ready()
	{
		camera = GetNode<Camera3D>("Camera3D");
        Input.MouseMode = Input.MouseModeEnum.Captured;
        bulletScene = (PackedScene)ResourceLoader.Load("res://scenes/Bullet.tscn");
	}

	// Called every frame. 'delta' is the elapsed time since the previous frame.
	public override void _Process(double delta)
	{
		HandleMovement(delta);
        HandleMouseInput(delta);
        //UpdateCameraPosition(delta);
        HandleFiring(delta);

	}

	private void HandleMovement(double delta)
    {
        // if (Input.IsActionPressed("move_forward"))
        // {
        //     Translate(Vector3.Forward * speed * (float)delta);
        // }

        // Update target roll based on input
        if (Input.IsActionPressed("roll_left"))
        {
            targetRoll = -rollSpeed;
        }
        else if (Input.IsActionPressed("roll_right"))
        {
            targetRoll = rollSpeed;
        }
        else
        {
            targetRoll = 0.0f;
        }

        // Smoothly interpolate current roll towards the target roll
        currentRoll = Mathf.Lerp(currentRoll, targetRoll, 5.0f * (float)delta);

        // Apply the roll rotation
        RotateObjectLocal(Vector3.Forward, currentRoll * (float)delta);

        // Smoothly interpolate current speed towards the target speed
        float targetSpeed = Input.IsActionPressed("move_forward") ? maxSpeed : 0.0f;
        currentSpeed = Mathf.Lerp(currentSpeed, targetSpeed, acceleration * (float)delta);

        // Move the ship forward based on the current speed
        Translate(Vector3.Forward * currentSpeed * (float)delta);
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

        // Handle mouse button press for firing bullets
        if (@event is InputEventMouseButton mouseButtonEvent)
        {
            if (mouseButtonEvent.ButtonIndex == MouseButton.Left)
            {
                isFiring = mouseButtonEvent.Pressed;
            }
        }
	}

    private void HandleFiring(double delta)
    {
        if (isFiring)
        {
            timeSinceLastShot += (float)delta;
            float timeBetweenShots = 1.0f / fireRate;

            while (timeSinceLastShot >= timeBetweenShots)
            {
                FireBullet();
                timeSinceLastShot -= timeBetweenShots;
            }
        }
    }

    private void FireBullet()
    {
        // Instance the bullet scene
        Bullet bullet = (Bullet)bulletScene.Instantiate();

        // Set the bullet's position and orientation to match the ship's
        bullet.GlobalTransform = this.GlobalTransform;

        // Add the bullet to the scene
        GetParent().AddChild(bullet);
    }

    // private void UpdateCameraPosition(double delta)
    // {
    //     if (camera == null)
    //     {
    //         return;
    //     }

    //     Vector3 targetPosition = GlobalTransform.Origin;
    //     Vector3 cameraPosition = camera.GlobalTransform.Origin;

    //     // Calculate direction while locking the Y axis
    //     Vector3 direction = (new Vector3(cameraPosition.X, 0, cameraPosition.Z) - new Vector3(targetPosition.X, 0, targetPosition.Z)).Normalized();

    //     // Calculate the desired position
    //     Vector3 desiredPosition = targetPosition + direction * cameraDistance;
    //     desiredPosition.Y = targetPosition.Y + fixedYDistance;

    //     // Interpolate the position smoothly
    //     Vector3 interpolatedPosition = new Vector3(
    //         Mathf.Lerp(cameraPosition.X, desiredPosition.X, cameraSmoothSpeed * (float)delta),
    //         desiredPosition.Y, // Keep Y position fixed
    //         Mathf.Lerp(cameraPosition.Z, desiredPosition.Z, cameraSmoothSpeed * (float)delta)
    //     );

    //     // Update the camera's transform
    //     camera.GlobalTransform = new Transform3D(camera.GlobalTransform.Basis, interpolatedPosition);
    //     camera.LookAt(new Vector3(targetPosition.X, targetPosition.Y + fixedYDistance, targetPosition.Z), new Vector3(0, 1, 0));
    // }
}
