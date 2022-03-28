clear vars;
clc;

%% Define Sampler
fH = 100;  %highest freq
fl = 1; %lowest freq
n = 100; %no of cycles to be detected

TH = 1/fH;  % shortest time period 
Tl = 1/fl;
Ts = TH/4;    % Sampling time period for 4 samples of each wavelet

t = 0:Ts:n*TH;  %define time vector for time domain
L = length(t); %Length of signal

Fs = 1/Ts;  %Sampling freq
Fn = Fs/2;  %Nyqiust freq

%% Input Signals
X1 = 3*sin(2*pi*20*t);
X2 = 5*sin(2*pi*40*t + pi/3);
noise = 2*randn(size(t))

%% Signal Arithmetic
X = X1 + X2;

%% Time domain to frequncy domain conversion
Nf = L;
f = linspace(0,Fn,Nf/2) %frequency vector
Y = fft(X,Nf);  %fast fourier transform
P2 = abs(Y/L);  %two sided spectrum
P1 = 2*P2(1:L/2)    %single sided spectrum

%% Plots
subplot(3,1,1); plot(t,[X1;X2]); title('Input Signals X1(t) & X2(t)'); xlabel('Time (sec)'); ylabel('Amplitude X(t)');ylim(1.2*[min(X2) max(X2)]); grid on;
subplot(3,1,2); plot(t,X); title('Output Signal X(t)'); xlabel('Time (sec)'); ylabel('Amplitude X(t)');ylim(1.2*[min(X) max(X)]); grid on;
subplot(3,1,3); plot(f,P1); title('signals in frequency domain'); xlabel('Frequency'); ylabel('|P1(f)|');ylim(1.2*[min(P1) max(P1)]); grid on;
