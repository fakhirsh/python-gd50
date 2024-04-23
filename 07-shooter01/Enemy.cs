using Godot;
using System;

public partial class Enemy : Node2D
{
	// Player reference
	private Node2D player;
	// Called when the node enters the scene tree for the first time.
	public override void _Ready()
	{
		player = GetNode<Node2D>("../Player");

		var area = GetNode<Area2D>("EnemyArea2D");
		area.Connect("area_entered", new Callable(this, nameof(OnCollision)));
		// area.Connect("body_entered", new Callable(this, nameof(OnCollision)));
	}

	
	private void OnCollision(Node body)
	{
		GD.Print("Collision with " + body.Name);
		if(body.GetParent() is Player player){
			player.Lives--;
			if (player.Lives <= 0)
			{
				player.QueueFree();
			}
		}
	}

	// Called every frame. 'delta' is the elapsed time since the previous frame.
	public override void _Process(double delta)
	{
		Position += (player.Position - Position).Normalized() * 100 * (float)delta;
		Rotation = (player.Position - Position).Angle();
	}
}
