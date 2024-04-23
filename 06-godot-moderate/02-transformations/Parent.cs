using Godot;
using System;

public partial class Parent : Sprite2D
{
	//get reference to child node
	private Sprite2D child1, child2;
	[Export]
	private bool toggleLocal {get;set;} = false;
	[Export]
	private int SPEED {get;set;} = 5;
	// Called when the node enters the scene tree for the first time.
	public override void _Ready()
	{
		//get reference to child node
		child1 = GetNode<Sprite2D>("Child1");
		child2 = GetNode<Sprite2D>("Child2");
	}

	// Called every frame. 'delta' is the elapsed time since the previous frame.
	public override void _Process(double delta)
	{
		// handle input
		if (Input.IsActionPressed("ui_right"))
		{
			if(!toggleLocal){
				child1.Position += new Vector2(SPEED, 0);
				child2.Position += new Vector2(SPEED, 0);
			}else{
				child1.Position += child1.Transform.X.Normalized() * SPEED;
				child2.Position += child2.Transform.X.Normalized() * SPEED;
			}
		}
		if (Input.IsActionPressed("ui_left"))
		{
			if(!toggleLocal){
				child1.Position += new Vector2(-SPEED, 0);
				child2.Position += new Vector2(-SPEED, 0);
			}else{
				child1.Position += child1.Transform.X.Normalized() * -1 * SPEED;
				child2.Position += child2.Transform.X.Normalized() * -1 * SPEED;
			}
		}
		if (Input.IsActionPressed("ui_up"))
		{
			this.RotationDegrees   += (float)(60.0 * 1.0 * delta);
			child1.RotationDegrees += (float)(60.0 * 1.5 * delta);
			child2.RotationDegrees += (float)(60.0 * 2.0 * delta);
		}
	}

	// _Input method override, handle right arrow key pressed
	public override void _Input(InputEvent @event)
	{
		if (@event is InputEventKey eventKey)
		{
			if (eventKey.Pressed && eventKey.Keycode == Key.Space)
			{
				toggleLocal = !toggleLocal;
			}
		}
	}



}
