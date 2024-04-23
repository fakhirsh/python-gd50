using Godot;
using System;

public partial class Bullet : Node2D
{
	// Called when the node enters the scene tree for the first time.
	private Sprite2D billetImg;
	[Export]
	public int SPEED = 1000; // How fast the player will move (pixels/sec);
	private float distance = 0;
	[Export]
	public float MAX_DISTANCE = 500;
	public override void _Ready()
	{
		billetImg = GetNode<Sprite2D>("bulletImg");
		var area = GetNode<Area2D>("BulletArea2D");
		area.Connect("area_entered", new Callable(this, nameof(OnCollision)));
		area.Connect("body_entered", new Callable(this, nameof(OnCollision)));
	}

	private void OnCollision(Node body)
	{
		GD.Print("Collision with " + body.Name);
		//QueueFree();
		body.GetParent().QueueFree();
	}

	// Called every frame. 'delta' is the elapsed time since the previous frame.
	public override void _Process(double delta)
	{
		Position += this.Transform.X.Normalized() * (float)(SPEED * delta);
		distance += (float)(SPEED * delta);
		if (distance > MAX_DISTANCE)
		{
			QueueFree();
		}
	}
}
