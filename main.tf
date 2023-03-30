resource "aws_lb" "example" {
  name               = "example"
  internal           = false
  load_balancer_type = "application"

  subnets = [
    "subnet-0f3b343cbd76d727e",
    "subnet-048acfcfcdfe570f5",
    "subnet-08153f53dda6f1ac0",
  ]

  security_groups = [
   "sg-0123456789abcdef0" #Internet access for the ALB
    #"sg-0123456789abcdef1", #Template came with 2
  ]
}

resource "aws_lb_listener" "example" {
  load_balancer_arn = aws_lb.example.arn
  port              = 80
  protocol          = "HTTP"

  default_action {
    target_group_arn = aws_lb_target_group.example.arn
    type             = "forward"
  }
}

resource "aws_lb_target_group" "example" {
  name        = "example"
  port        = 8000
  protocol    = "HTTP"
  target_type = "ip"

  vpc_id = "vpc-020e420d4ad91eaad"
}

resource "aws_ecs_task_definition" "example" {
  family                   = "example"
  container_definitions    = jsonencode([
    {
      name  = "example"
      image = "rockadeus/academy-sre-bootcamp-paul-furlan:latest"
      portMappings = [
        {
          containerPort = 8000
          hostPort      = 0
        }
      ]
    }
  ])
  requires_compatibilities = ["FARGATE"]
  network_mode             = "awsvpc"
  cpu                      = "256"
  memory                   = "512"
}

resource "aws_ecs_service" "example" {
  name            = "example"
  cluster         = "default"
  task_definition = aws_ecs_task_definition.example.arn
  desired_count   = 1

  network_configuration {
    assign_public_ip = true
    subnets          = [
      "subnet-0f3b343cbd76d727e",
      "subnet-048acfcfcdfe570f5",
      "subnet-08153f53dda6f1ac0",
    ]

    security_groups = [
      "sg-068ee5df932fd38ff"
      #"sg-0123456789abcdef0",
      #"sg-0123456789abcdef1",
    ]
  }

  load_balancer {
    target_group_arn = aws_lb_target_group.example.arn
    container_name   = "example"
    container_port   = 8000
  }
}
