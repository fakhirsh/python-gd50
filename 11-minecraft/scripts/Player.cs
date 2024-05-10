using Godot;
using System;

public partial class Player : CharacterBody3D
{
	public const float Speed = 8.0f;
	public const float JumpVelocity = 8f;

	// Get the gravity from the project settings to be synced with RigidBody nodes.
	//public float gravity = ProjectSettings.GetSetting("physics/3d/default_gravity").AsSingle();
	public float gravity = 16f;

// Mouse look variables
    private const float MouseSensitivity = 0.003f;
    private float _rotationX;
    private float _rotationY;

	// Ready
	public override void _Ready()
	{
		
		Input.MouseMode = Input.MouseModeEnum.Captured;
	}

	public override void _PhysicsProcess(double delta)
	{
		Vector3 velocity = Velocity;

		// Add the gravity.
		if (!IsOnFloor())
			velocity.Y -= gravity * (float)delta;

		// Handle Jump.
		if (Input.IsActionJustPressed("jump") && IsOnFloor())
			velocity.Y = JumpVelocity;

		// Get the input direction and handle the movement/deceleration.
		// As good practice, you should replace UI actions with custom gameplay actions.
		Vector2 inputDir = Input.GetVector("left", "right", "forward", "back");
		Vector3 direction = (Transform.Basis * new Vector3(inputDir.X, 0, inputDir.Y)).Normalized();
		if (direction != Vector3.Zero)
		{
			velocity.X = direction.X * Speed;
			velocity.Z = direction.Z * Speed;
		}
		else
		{
			velocity.X = Mathf.MoveToward(Velocity.X, 0, 0.5f);
			velocity.Z = Mathf.MoveToward(Velocity.Z, 0, 0.5f);
		}

		var ray = GetNode<RayCast3D>("Camera3D/RayCast3D");

		if (Input.IsActionJustPressed("left_click")){
			//GD.Print("Left Click");
			if (ray.IsColliding()){
				//GD.Print("Colliding with something");
				var collider = ray.GetCollider();
                if (collider != null)
                {
                    //GD.Print($"Colliding with: {collider}");
                    //GD.Print($"Type: {collider.GetType().Name}");
					if (collider is GridMap map)
					{
						GD.Print("Colliding with gridmap");
						map.AddBlock(ray.GetCollisionPoint() + ray.GetCollisionNormal() * 0.1f, 1);
					}
                }

			}
		}
		if (Input.IsActionJustPressed("right_click")){
			if (ray.IsColliding()){
				var collider = ray.GetCollider();
                if (collider != null)
                {
					if (collider is GridMap map)
					{
						map.DestroyBlock(ray.GetCollisionPoint() - ray.GetCollisionNormal() * 0.1f);
					}
                }

			}
		}

		Velocity = velocity;
		MoveAndSlide();
	}

    public override void _UnhandledInput(InputEvent @event)
    {
        // Handle mouse look
		if (@event is InputEventMouseMotion mouseMotion)
		{
			Rotation = new Vector3(
				Rotation.X - mouseMotion.Relative.Y * MouseSensitivity,
				Rotation.Y - mouseMotion.Relative.X * MouseSensitivity,
				0
			);
		}

    }

    
}
