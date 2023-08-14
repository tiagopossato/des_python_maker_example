from supervisor import Events, trigger_event
# from handle_event import trigger_event
from time import sleep

from factoryIOInterface import *
#-------- CAMADA FÍSICA ENTRADAS ----------------
def s1_action(value):
    if(value == True):
        trigger_event(Events['t1'])

s1_input.set_callback(s1_action)

def s2_action(value):
    if(value == True):
        trigger_event(Events['t2'])

s2_input.set_callback(s2_action)

def ppx_moving_action(value):
    if(value == True):
        trigger_event(Events['m7'])
    else:
        trigger_event(Events['p7'])

ppx_moving_input.set_callback(ppx_moving_action)

def ppz_moving_action(value):
    if(value == True):
        trigger_event(Events['m6'])
    else:
        trigger_event(Events['p6'])

ppz_moving_input.set_callback(ppz_moving_action)

def ppg_item_action(value):
    if(value == True):
        trigger_event(Events['t5'])

ppg_item_input.set_callback(ppg_item_action)

def start_action(value):
    if(value == True):
        trigger_event(Events['t3'])

start_input.set_callback(start_action)

def stop_action(value):
    if(value == False):
        trigger_event(Events['t4'])

stop_input.set_callback(stop_action)

def reset_action(value):
    if(value == True):
        #print messagem in red collor
        print("\033[91m" + "\n\n Reset pressionado \n\n" + "\033[0m")
        exit(0)
reset_input.set_callback(reset_action)

def cv1_on_action(event):
    cv1.on()

def cv1_off_action(event):
    cv1.off()

def cv2_on_action(event):
    cv2.on()

def cv2_off_action(event):
    cv2.off()

def ppx_on_action(event):
    ppx.on()

def ppx_off_action(event):
    ppx.off()

def ppg_on_action(event):
    ppg.on()

def ppg_off_action(event):
    ppg.off()

def ppz_on_action(event):
    ppz.on()

def ppz_off_action(event):
    ppz.off()

Events['s1'].set_action(cv1_on_action)
Events['f1'].set_action(cv1_off_action)
Events['s2'].set_action(cv2_on_action)
Events['f2'].set_action(cv2_off_action)
Events['s4'].set_action(ppx_on_action)
Events['f4'].set_action(ppx_off_action)
Events['s5'].set_action(ppg_on_action)
Events['f5'].set_action(ppg_off_action)
Events['s3'].set_action(ppz_on_action)
Events['f3'].set_action(ppz_off_action)

if __name__ == '__main__':
    sleep(2)
    while True:
        try:
            read_all_input_values()
            sleep(.01)
        except Exception as e:
            print(e)
        except KeyboardInterrupt:            
            print("Interrompendo a simulação, aguarde o encerramento...")
            break
