%%
rosinit; %Conexion con nodo maestro
%%
velPub = rospublisher('/turtle1/cmd_vel','geometry_msgs/Twist'); %Creacion publicador
velMsg = rosmessage(velPub);                                     %Creacion de mensaje
teleport = rossvcclient('/turtle1/teleport_absolute', 'turtlesim/TeleportAbsolute');
telReq = rosmessage(teleport);
%%
telReq.X = 5.4;
telReq.Y = 3.2;
telReq.Theta = pi/2;
call(teleport, telReq)
%%
velMsg.Linear.X = 1;
velMsg.Linear.Y = 1;
velMsg.Angular.Z = 3;
send(velPub,velMsg);
pause(1)
%% 
suscrPose = rossubscriber("/turtle1/pose",'turtlesim/Pose');
suscrPose.LatestMessage
%%
rosshutdown