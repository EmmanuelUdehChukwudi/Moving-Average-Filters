import serial
import time
import matplotlib.pyplot as plt

def sma_filter(data_points, window_size=10):
    sma_list = []
    for i in range(len(data_points) - window_size + 1):
        window = data_points[i:i + window_size]
        sma = sum(window) / window_size
        sma_list.append(sma)
    return sma_list

def read_from_serial(port, window_size=10):
    raw_data_points = []
    filtered_data_points = []
    
    try:
        ser = serial.Serial(port, 9600, timeout=1)
        time.sleep(2)
        
        plt.ion() 
        fig, ax = plt.subplots()
        raw_line, = ax.plot([], [], label='Raw Data')
        filtered_line, = ax.plot([], [], label='Filtered Data (SMA)')
        ax.legend()
        
        while True:
            try:
                line = ser.readline()
                try:
                    line = line.decode().strip()
                except UnicodeDecodeError as e:
                    print(f"Decode error: {e}")
                    continue

                if line:
                    angles = line.split(',')
                    if len(angles) == 3:
                        z_angle = float(angles[2])
                        raw_data_points.append(z_angle)
                        if len(raw_data_points) >= window_size:
                            res = sma_filter(raw_data_points, window_size)
                            filtered_data_points.append(res[-1])
                        else:
                            filtered_data_points.append(z_angle)
                        
                        raw_line.set_data(range(len(raw_data_points)), raw_data_points)
                        filtered_line.set_data(range(len(filtered_data_points)), filtered_data_points)
                        ax.relim()
                        ax.autoscale_view()
                        plt.draw()
                        plt.pause(0.0001)  
            except Exception as e:
                print(f"Error reading line: {e}")
                break
    except Exception as e:
        print(f"Failed to open serial port: {e}")
    finally:
        if 'ser' in locals() and ser.is_open:
            ser.close()
            print("Serial port closed.")

if __name__ == "__main__":
    # port = input("Enter the serial port (e.g., COM3 or /dev/ttyUSB0): ")
    port = "/dev/ttyUSB0"
    read_from_serial(port)
