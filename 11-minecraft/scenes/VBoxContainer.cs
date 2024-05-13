using Godot;
using System;

public partial class VBoxContainer : Godot.VBoxContainer
{
	// Called when the node enters the scene tree for the first time.
	Button quitButton;
	Button newGameButton;

	private PackedScene worldScene; 

	public override void _Ready()
	{
		worldScene = GD.Load<PackedScene>("res://scenes/World.tscn");

		newGameButton = GetNode<Button>("NewGameButton");
		newGameButton.Connect("pressed", new Callable(this, nameof(OnNewGamePressed)));
		quitButton = GetNode<Button>("QuitButton");
		quitButton.Connect("pressed", new Callable(this, nameof(OnQuitPressed)));
	}

	// Called every frame. 'delta' is the elapsed time since the previous frame.
	public override void _Process(double delta)
	{
	}

	public void OnNewGamePressed()
	{
		GetTree().ChangeSceneToPacked(worldScene);
	}
	void OnQuitPressed()
	{
		GetTree().Quit();
	}
}
