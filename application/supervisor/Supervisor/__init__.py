from .Base import Event, EventKind, State, Supervisor
from .events import Events, get_event_by_id
from .logger import log_error, log_state
from .supervisors import supE01_liga_cv1,supE02_desliga_cv1,supE03_bloqueia_braco,supE04_desce_braco,supE05_sobre_braco,supE06_avanca_braco,supE07_retorna_braco,supE08_pega_peca,supE09_solta_peca,supE10_liga_cv2,supE11_desliga_cv2
supervisors_list = [supE01_liga_cv1,supE02_desliga_cv1,supE03_bloqueia_braco,supE04_desce_braco,supE05_sobre_braco,supE06_avanca_braco,supE07_retorna_braco,supE08_pega_peca,supE09_solta_peca,supE10_liga_cv2,supE11_desliga_cv2]
# import trigger_event after supervisor_list for avoid circular import
from .handle_event import trigger_event
