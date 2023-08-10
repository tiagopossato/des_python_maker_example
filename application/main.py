from supervisor import Events, trigger_event
# from handle_event import trigger_event
from time import sleep

from factoryIOInterface import *
#-------- CAMADA FÍSICA ENTRADAS ----------------
def s1_action(value):
    if(value == True):
        trigger_event(Events['s1'])

s1_input.set_callback(s1_action)

def s2_action(value):
    if(value == True):
        trigger_event(Events['s2'])

s2_input.set_callback(s2_action)

def ppx_moving_action(value):
    if(value == True):
        trigger_event(Events['ppx_moving'])
    else:
        trigger_event(Events['ppx_stoped'])

ppx_moving_input.set_callback(ppx_moving_action)

def ppz_moving_action(value):
    if(value == True):
        trigger_event(Events['ppz_moving'])
    else:
        trigger_event(Events['ppz_stoped'])

ppz_moving_input.set_callback(ppz_moving_action)

def ppg_item_action(value):
    if(value == True):
        trigger_event(Events['ppg_item'])

ppg_item_input.set_callback(ppg_item_action)

def start_action(value):
    if(value == True):
        trigger_event(Events['start'])

start_input.set_callback(start_action)

def stop_action(value):
    if(value == False):
        trigger_event(Events['stop'])

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

Events['cv1_on'].set_action(cv1_on_action)
Events['cv1_off'].set_action(cv1_off_action)
Events['cv2_on'].set_action(cv2_on_action)
Events['cv2_off'].set_action(cv2_off_action)
Events['ppx_on'].set_action(ppx_on_action)
Events['ppx_off'].set_action(ppx_off_action)
Events['ppg_on'].set_action(ppg_on_action)
Events['ppg_off'].set_action(ppg_off_action)
Events['ppz_on'].set_action(ppz_on_action)
Events['ppz_off'].set_action(ppz_off_action)

if __name__ == '__main__':
    sleep(3)
    while True:
        try:
            read_all_input_values()
            sleep(.01)
        except Exception as e:
            print(e)
        except KeyboardInterrupt:            
            print("Interrompendo a simulação, aguarde o encerramento...")
            break
