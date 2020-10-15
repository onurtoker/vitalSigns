pkg load zeromq
 
num_data=2040;

figure(1);  clf;
% ZMQ
sock1 = zmq_socket(ZMQ_SUB);  % socket-connect-opt-close = 130 us
zmq_connect(sock1,"tcp://127.0.0.1:5555");
zmq_setsockopt(sock1, ZMQ_SUBSCRIBE, "");

L=[];
for k=1:100
  recv=zmq_recv(sock1, num_data*8, 0); 
  vector=typecast(recv,"single complex"); % char -> float
  %plot(real(vector),'b-'); hold on;
  V=fft(vector);
  [mx,ix]=max(abs(V));
  L=[L angle(V(ix))];  
end

zmq_close (sock1);

%figure(2);
plot(L*180/pi,'linewidth',2);
ylim([-180,180]);


