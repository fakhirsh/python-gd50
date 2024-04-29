using Godot;
using System;

public partial class Dino : CharacterBody2D
{
	public const float Speed = 500.0f;
	public const float JumpVelocity = -1500.0f;

	// Get the gravity from the project settings to be synced with RigidBody nodes.
	public float gravity = ProjectSettings.GetSetting("physics/2d/default_gravity").AsSingle();

	public override void _PhysicsProcess(double delta)
	{
		Vector2 velocity = Velocity;

		var animatedSprite = GetNode<AnimatedSprite2D>("AnimatedSprite2D");

		if (IsOnFloor()){
			if(!GetParent<Main>().gameRunning){
				animatedSprite.Play("idle");
			}
			else{			
				var runningColShape = GetNode<CollisionShape2D>("RunCol");
				runningColShape.Disabled = false;

				if (Input.IsActionPressed("dino_jump")){
					velocity.Y = JumpVelocity;
					var jumpSound = GetNode<AudioStreamPlayer2D>("JumpSound");
					jumpSound.Play();
				}
				else if (Input.IsActionPressed("dino_duck")){
					animatedSprite.Play("duck");
					runningColShape.Disabled = true;
				}
				else{
					animatedSprite.Play("run");
				}
			}
		}
		else{
			velocity.Y += gravity * (float)delta;
			animatedSprite.Play("jump");
		}

		Velocity = velocity;
		MoveAndSlide();
	}
}
