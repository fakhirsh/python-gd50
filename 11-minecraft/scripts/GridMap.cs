using Godot;
using System;

public partial class GridMap : Godot.GridMap
{
	// Called when the node enters the scene tree for the first time.
	public override void _Ready()
	{
	}

	// Called every frame. 'delta' is the elapsed time since the previous frame.
	public override void _Process(double delta)
	{
	}

	// Create a function called DestroyBlock(world_position) that takes a Vector3 world_position as an argument.
	// This function will remove the block at the given world position.
	public void DestroyBlock(Vector3 world_position)
	{
		// Convert the world position to a grid position.
		Vector3I grid_position = LocalToMap(world_position);
		SetCellItem(grid_position, -1);
	}

	// Create a function called PlaceBlock(world_position, block_index) that takes a Vector3 world_position and an integer block_index as arguments.
	// This function will place a block at the given world position with the given block index.
	public void AddBlock(Vector3 world_position, int block_index)
	{
		// Convert the world position to a grid position.
		Vector3I grid_position = LocalToMap(world_position);
		SetCellItem(grid_position, block_index);
	}
}
