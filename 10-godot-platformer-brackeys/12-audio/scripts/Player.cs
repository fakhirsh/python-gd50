using Godot;
using System;

public partial class Player : CharacterBody2D
{
	public const float Speed = 130.0f;
	public const float JumpVelocity = -300.0f;

	// Get the gravity from the project settings to be synced with RigidBody nodes.
	public float gravity = ProjectSettings.GetSetting("physics/2d/default_gravity").AsSingle();

	public override void _PhysicsProcess(double delta)
	{
		Vector2 velocity = Velocity;

		var animSprite = GetNode<AnimatedSprite2D>("AnimatedSprite2D");

		// Add the gravity.
		if (!IsOnFloor()){
			velocity.Y += gravity * (float)delta;
			animSprite.Play("jump");			
		}
		// Handle Jump.
		if (Input.IsActionJustPressed("jump") && IsOnFloor()){
			velocity.Y = JumpVelocity;
		}

		float direction = Input.GetAxis("move_left", "move_right");
		if (direction < 0)
		{
			animSprite.FlipH = true;
			
		}
		else if (direction > 0)
		{
			animSprite.FlipH = false;
			
		}
		if (IsOnFloor()){
			if(direction == 0){
				animSprite.Play("idle");
			}
			else{
				animSprite.Play("run");
			}
		}

		velocity.X = direction * Speed;

		Velocity = velocity;
		MoveAndSlide();
	}
}
