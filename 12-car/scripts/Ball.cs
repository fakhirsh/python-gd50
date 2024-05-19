using Godot;
using System;

public partial class Ball : Node3D
{
	int acceleration = 1;

    // Camera follow speed
    float cameraFollowSpeed = 2.0f;
    // Camera distance from the ball
    float cameraDistance = 3.0f;
	// Vertical offset for the camera
    float verticalOffset = 5.0f;
    // Damping factor for vertical movement
    float verticalDamping = 0.1f;

    RigidBody3D ballRB;
    Camera3D camera;

    public override void _Ready()
    {
        ballRB = GetNode<RigidBody3D>("RigidBody3D");
        camera = GetNode<Camera3D>("Camera3D");

        if (camera != null && ballRB != null)
        {
            Vector3 initialBallPos = ballRB.GlobalTransform.Origin;
            Vector3 initialCameraPos = initialBallPos + camera.GlobalTransform.Basis.X * cameraDistance + new Vector3(0, 1, 0);
            camera.GlobalTransform = new Transform3D(camera.GlobalTransform.Basis, initialCameraPos);
            camera.LookAt(initialBallPos, Vector3.Up);
        }
    }

    public override void _PhysicsProcess(double delta)
    {
		Vector3 ballVelocity;
        var inputDirection = new Vector3(0, 0, 0);

        // Update input direction based on player input and camera orientation
        if (Input.IsActionPressed("move_forward"))
        {
            inputDirection -= camera.GlobalTransform.Basis.Z;
        }
        if (Input.IsActionPressed("move_backward"))
        {
            inputDirection += camera.GlobalTransform.Basis.Z;
        }
        if (Input.IsActionPressed("move_left"))
        {
            inputDirection -= camera.GlobalTransform.Basis.X;
        }
        if (Input.IsActionPressed("move_right"))
        {
            inputDirection += camera.GlobalTransform.Basis.X;
        }

        // Apply force to the ball in the direction of input adjusted for current motion
        if (inputDirection.Length() > 0)
        {
            ballVelocity = ballRB.LinearVelocity.Normalized();
            var direction = (ballVelocity + inputDirection).Normalized();
            ballRB.ApplyCentralImpulse(direction * acceleration);
        }

        // Update the camera position to follow the ball
        Vector3 ballPos = ballRB.GlobalTransform.Origin;
        ballVelocity = ballRB.LinearVelocity;

        if (ballVelocity.Length() > 0.1f) // Add a small threshold to avoid jittering when the ball is nearly stationary
        {
            Vector3 targetCameraPos = ballPos - ballVelocity.Normalized() * cameraDistance + new Vector3(0, 5, 0);
			targetCameraPos.Y = Mathf.Lerp(camera.GlobalTransform.Origin.Y, ballPos.Y + verticalOffset, verticalDamping);

            camera.GlobalTransform = new Transform3D(camera.GlobalTransform.Basis, camera.GlobalTransform.Origin.Lerp(targetCameraPos, cameraFollowSpeed * (float)delta));
        }

        // Make the camera look at the ball
        camera.LookAt(ballPos, Vector3.Up);
    }
}
