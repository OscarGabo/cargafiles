from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.core.mail import send_mail, EmailMessage
from django.core.mail import EmailMultiAlternatives
from datetime import datetime, date, time, timedelta
import calendar
from ftplib import FTP
import requests


def index(request):
    template = loader.get_template('cargafiles/index.html')
    titulo = 'CargaFiles'

    unidades_operativas = [
        {
            "nomen": "rci",
            "nombre": "Coecillo",
            "rutas": ['RCI355', 'RCI354', 'RCI353', 'RCI352', 'RCI351', 'RCI350', 'RCI343',
                      'RCI342', 'RCI341', 'RCI340', 'RCI270', 'RCI269', 'RCI268', 'RCI267',
                      'RCI266', 'RCI265', 'RCI264', 'RCI263', 'RCI262', 'RCI177', 'RCI176',
                      'RCI175', 'RCI174', 'RCI173', 'RCI172', 'RCI171', 'RCI170', 'RCI169',
                      'RCI168', 'RCI167', 'RCI166', 'RCI165', 'RCI164', 'RCI163', 'RCI162',
                      'RCI161', 'RCI160', 'RCI159', 'RCI158', 'RCI157', 'RCI156', 'RCI155',
                      'RCI154', 'RCI153', 'RCI152', 'RCI151', 'RCI150', 'RCI149', 'RCI148',
                      'RCI147', 'RCI146', 'RCI145', 'RCI144', 'RCI143', 'RCI142', 'RCI141',
                      'RCI140', 'RCI139', 'RCI138', 'RCI137', 'RCI136', 'RCI135', 'RCI134',
                      'RCI133', 'RCI132', 'RCI131', 'RCI130', 'RCI129', 'RCI128', 'RCI127',
                      'RCI126', 'RCI125', 'RCI124', 'RCI123', 'RCI122', 'RCI121', 'RCI120',
                      'RCI119', 'RCI118', 'RCI117', 'RCI116', 'RCI115', 'RCI114', 'RCI113',
                      'RCI112', 'RCI111', 'RCI110', 'RCI109', 'RCI108', 'RCI107', 'RCI106',
                      'RCI105', 'RCI104', 'RCI103', 'RCI102', 'RCI101']
        }, {
            "nomen": "rol",
            "nombre": "Leon",
            "rutas": ['ROL486', 'ROL485', 'ROL468', 'ROL467', 'ROL466', 'ROL465', 'ROL464',
                      'ROL463', 'ROL462', 'ROL493', 'ROL461', 'ROL438', 'ROL436', 'ROL435',
                      'ROL434', 'ROL433', 'ROL431', 'ROL415', 'ROL402', 'ROL400', 'ROL354',
                      'ROL353', 'ROL349', 'ROL337', 'ROL492', 'ROL183', 'ROL141', 'ROL137',
                      'ROL130', 'ROL129', 'ROL128', 'ROL127', 'ROL126', 'ROL125', 'ROL120',
                      'ROL119', 'ROL117', 'ROL114', 'ROL113', 'ROL111', 'ROL105', 'ROL104',
                      'ROL103', 'ROL102', 'ROL101', 'ROL084', 'ROL083', 'ROL082', 'ROL081',
                      'ROL080', 'ROL079', 'ROL078', 'ROL077', 'ROL076', 'ROL075', 'ROL074',
                      'ROL073', 'ROL072', 'ROL071', 'ROL070', 'ROL491', 'ROL490', 'ROL069',
                      'ROL068', 'ROL060', 'ROL059', 'ROL058', 'ROL057', 'ROL056', 'ROL055',
                      'ROL054', 'ROL053', 'ROL489', 'ROL052', 'ROL051', 'ROLD07', 'ROLD06',
                      'ROLD05', 'ROLD04', 'ROLD03', 'ROL702', 'ROL050', 'ROL049', 'ROL048',
                      'ROL047', 'ROL046', 'ROL045', 'ROL044', 'ROL043', 'ROL042', 'ROL499',
                      'ROL498', 'ROL497', 'ROL488', 'ROL040', 'ROL039', 'ROL029', 'ROL028',
                      'ROL027', 'ROL024', 'ROL023', 'ROL022', 'ROL021', 'ROL012', 'ROL011',
                      'ROL010', 'ROL009', 'ROLTE8', 'ROLTE7', 'ROLTE6', 'ROLTE5', 'ROLTE4',
                      'ROLTE3', 'ROLTE2', 'ROLTE1', 'ROLT11', 'ROL008', 'ROL007', 'ROL006',
                      'ROLT10', 'ROLT09', 'ROLT07', 'ROLT06', 'ROLT05', 'ROLT04', 'ROLT03',
                      'ROLT02', 'ROLT01', 'ROLD15', 'ROLD14', 'ROLD13', 'ROLD12', 'ROLD11',
                      'ROLD10', 'ROLD09', 'ROLD08', 'ROL496', 'ROL495', 'ROL494', 'ROL487']
        }, {
            "nomen": "rcl",
            "nombre": "Celaya",
            "rutas": ['RCL001', 'RCL008', 'RCL010', 'RCL014', 'RCL018', 'RCL023', 'RCL025',
                      'RCL026', 'RCL027', 'RCL031', 'RCL033', 'RCL034', 'RCL036', 'RCL042',
                      'RCL056', 'RCL102', 'RCL103', 'RCL104', 'RCL105', 'RCL106', 'RCL107',
                      'RCL109', 'RCL111', 'RCL112', 'RCL113', 'RCL115', 'RCL116', 'RCL117',
                      'RCL119', 'RCL120', 'RCL121', 'RCL122', 'RCL123', 'RCL128', 'RCL129',
                      'RCL130', 'RCL132', 'RCL135', 'RCL137', 'RCL138', 'RCL139', 'RCL140',
                      'RCL141', 'RCL143', 'RCL144', 'RCL145', 'RCL146', 'RCL154', 'RCL155',
                      'RCLD01', 'RCLD02', 'RCLD03', 'RCLD04', 'RCLTC1', 'RCLTC2', 'RCLTC3']
        }, {
            "nomen": "rir",
            "nombre": "Irapuato",
            "rutas": ['RIR200', 'RIR201', 'RIR202', 'RIR203', 'RIR204', 'RIR205', 'RIR206',
                      'RIR207', 'RIR208', 'RIR209', 'RIR210', 'RIR211', 'RIR212', 'RIR213',
                      'RIR214', 'RIR215', 'RIR216', 'RIR217', 'RIR218', 'RIR219', 'RIR220',
                      'RIR221', 'RIR222', 'RIR223', 'RIR224', 'RIR225', 'RIR226', 'RIR227',
                      'RIR228', 'RIR229', 'RIR230', 'RIR231', 'RIR232', 'RIR233', 'RIR234',
                      'RIR235', 'RIR236', 'RIR237', 'RIR238', 'RIR239', 'RIR240', 'RIR241',
                      'RIR242', 'RIR243', 'RIR244', 'RIR245', 'RIR246', 'RIR247', 'RIR248',
                      'RIR249', 'RIR250', 'RIR251', 'RIR252', 'RIR253', 'RIR254', 'RIR255',
                      'RIR256', 'RIR257', 'RIR258', 'RIR259', 'RIR260', 'RIR261', 'RIR262',
                      'RIR263', 'RIR264', 'RIR265', 'RIR266', 'RIR267', 'RIR268', 'RIR269',
                      'RIR270', 'RIR271', 'RIR272', 'RIR273', 'RIRD01', 'RIRD02', 'RIRD03',
                      'RIRD04', 'RIRTC1', 'RIRTC2', 'RIRTC3', 'RIRTC6', 'RIRTE1', 'RIRTE2',
                      'RIRTE3', 'RIRD05', 'RIR017', 'RIR018', 'RIR022']
        }, {
            "nomen": "reu",
            "nombre": "Fresno",
            "rutas": ['REUR01', 'REUR02', 'REUR03', 'REUR04', 'REUR05', 'REUR06', 'REUR07',
                      'REUR08', 'REUR09', 'REUR10', 'REUR11', 'REUR12', 'REUR13', 'REUR14',
                      'REUR15', 'REUR16', 'REUR17', 'REUR18', 'REUR19', 'REUR20', 'REUR21',
                      'REUR22', 'REUR23', 'REUR24', 'REUR25', 'REUR26', 'REUR27', 'REUR28',
                      'REUR29', 'REUR30', 'REUR31', 'REUR32', 'REUR33', 'REUR34', 'REUR35',
                      'REUR36']
        }, {
            "nomen": "riz",
            "nombre": "Cedis Sur",
            "rutas": ['RIZ201', 'RIZ202', 'RIZ203', 'RIZ204', 'RIZ205', 'RIZ206', 'RIZ207',
                      'RIZ208', 'RIZ209', 'RIZ210', 'RIZ211', 'RIZ212', 'RIZ213', 'RIZ214',
                      'RIZ215', 'RIZ216', 'RIZ217', 'RIZ218', 'RIZ219', 'RIZ220', 'RIZ221',
                      'RIZ222', 'RIZ223', 'RIZ224', 'RIZ225', 'RIZ226', 'RIZ227', 'RIZ228',
                      'RIZ229', 'RIZ230', 'RIZ231', 'RIZ232', 'RIZ233', 'RIZ234', 'RIZ235',
                      'RIZ236', 'RIZ237', 'RIZ238', 'RIZ239', 'RIZ240', 'RIZ241', 'RIZ242',
                      'RIZ243', 'RIZ244', 'RIZ245', 'RIZ246', 'RIZ247', 'RIZ248', 'RIZ249',
                      'RIZ250', 'RIZ251', 'RIZ252', 'RIZ253', 'RIZ254', 'RIZ255', 'RIZ256',
                      'RIZ257', 'RIZ258', 'RIZ259', 'RIZ260', 'RIZ261', 'RIZ262', 'RIZ263',
                      'RIZ264', 'RIZ265', 'RIZ266', 'RIZ267', 'RIZ268', 'RIZ269', 'RIZ270',
                      'RIZ271', 'RIZ272', 'RIZ273', 'RIZ274', 'RIZ275', 'RIZ276', 'RIZ277',
                      'RIZ278', 'RIZ279', 'RIZ280', 'RIZ281', 'RIZ282', 'RIZ283', 'RIZ284',
                      'RIZ285', 'RIZ286', 'RIZ287', 'RIZ288', 'RIZ289', 'RIZ290', 'RIZ291',
                      'RIZ292', 'RIZ293', 'RIZ294', 'RIZ295', 'RIZ296', 'RIZ297', 'RIZ298',
                      'RIZ299', 'RIZ001', 'RIZ002', 'RIZ003', 'RIZ004', 'RIZ005', 'RIZ006',
                      'RIZ007', 'RIZ008', 'RIZ009', 'RIZ010', 'RIZ011', 'RIZ012', 'RIZ013',
                      'RIZ014', 'RIZ015', 'RIZ016', 'RIZ017', 'RIZ018', 'RIZ019', 'RIZ020',
                      'RIZ101', 'RIZ102', 'RIZ103', 'RIZ104', 'RIZ105', 'RIZ106', 'RIZ107',
                      'RIZ108', 'RIZ109', 'RIZ110', 'RIZ111', 'RIZ112', 'RIZ113', 'RIZ114',
                      'RIZ115', 'RIZ116', 'RIZ117', 'RIZ118', 'RIZ119', 'RIZ120', 'RIZ121',
                      'RIZ122', 'RIZ123', 'RIZ124', 'RIZ125', 'RIZ126', 'RIZ127', 'RIZ128',
                      'RIZ129', 'RIZ130', 'RIZ131', 'RIZ132', 'RIZ133', 'RIZ134', 'RIZ135',
                      'RIZ136', 'RIZ137', 'RIZ138', 'RIZ139', 'RIZ140', 'RIZ141', 'RIZ142',
                      'RIZ143', 'RIZ144', 'RIZ145', 'RIZ146', 'RIZ147', 'RIZ148', 'RIZ149',
                      'RIZ150', 'RIZ501', 'RIZ512', 'RIZ513', 'RIZ514', 'RIZ515', 'RIZ516',
                      'RIZ517', 'RIZ518', 'RIZ519', 'RIZ520']
        }, {
            "nomen": "rch",
            "nombre": "Chalco",
            "rutas": ['RCH101', 'RCH102', 'RCH103', 'RCH104', 'RCH105', 'RCH106', 'RCH107',
                      'RCH108', 'RCH109', 'RCH110', 'RCH111', 'RCH112', 'RCH113', 'RCH114',
                      'RCH115', 'RCH116', 'RCH117', 'RCH201', 'RCH202', 'RCH203', 'RCH204',
                      'RCH205', 'RCH206', 'RCH207', 'RCH208', 'RCH209', 'RCH210', 'RCH211',
                      'RCH212', 'RCH213', 'RCH214', 'RCH215', 'RCH216', 'RCH217', 'RCH218',
                      'RCH219', 'RCH301', 'RCH302', 'RCH303', 'RCH304', 'RCH305', 'RCH306',
                      'RCH307', 'RCH308', 'RCH309', 'RCH310', 'RCH311', 'RCH312', 'RCH313',
                      'RCH314', 'RCH315', 'RCH316', 'RCH317', 'RCH318', 'RCH401', 'RCH402',
                      'RCH403', 'RCH404', 'RCH405', 'RCH406', 'RCH407', 'RCH408', 'RCH409',
                      'RCH410', 'RCH411', 'RCH412', 'RCH413', 'RCH414', 'RCH415', 'RCH416',
                      'RCH417', 'RCH418', 'RCH419', 'RCH501', 'RCH502', 'RCH503', 'RCH504',
                      'RCH505', 'RCH506', 'RCH507', 'RCH508', 'RCH509', 'RCH510', 'RCH511',
                      'RCH512', 'RCH513', 'RCH514', 'RCH515', 'RCH516', 'RCH517', 'RCH518']
        }, {
            "nomen": "rmi",
            "nombre": "Mixcoac",
            "rutas": ['RMI101', 'RMI102', 'RMI103', 'RMI104', 'RMI105', 'RMI106', 'RMI107',
                      'RMI108', 'RMI109', 'RMI110', 'RMI111', 'RMI112', 'RMI113', 'RMI114',
                      'RMI115', 'RMI116', 'RMI201', 'RMI202', 'RMI203', 'RMI204', 'RMI205',
                      'RMI206', 'RMI207', 'RMI208', 'RMI209', 'RMI210', 'RMI211', 'RMI212',
                      'RMI213', 'RMI214', 'RMI215', 'RMI221', 'RMI301', 'RMI302', 'RMI303',
                      'RMI304', 'RMI305', 'RMI306', 'RMI307', 'RMI308', 'RMI309', 'RMI310',
                      'RMI311', 'RMI312', 'RMI313', 'RMI314', 'RMI315', 'RMI316', 'RMI317',
                      'RMI401', 'RMI402', 'RMI403', 'RMI404', 'RMI405', 'RMI406', 'RMI407',
                      'RMI408', 'RMI409', 'RMI410', 'RMI411', 'RMI412', 'RMI501', 'RMI502',
                      'RMI503', 'RMI504', 'RMI505', 'RMI506', 'RMI507', 'RMI508', 'RMI509',
                      'RMI510', 'RMI511', 'RMI512', 'RMI513', 'RMI514', 'RMI515', 'RMI516',
                      'RMIM01', 'RMIM02', 'RMIM03', 'RMIM04', 'RMIM05', 'RMIM06', 'RMIM07',
                      'RMIM08', 'RMIM09', 'RMIM10', 'RMIM11', 'RMIM12', 'RMIM13']
        }, {
            "nomen": "rry",
            "nombre": "Reyes",
            "rutas": ['RRY201', 'RRY202', 'RRY203', 'RRY204', 'RRY205', 'RRY206', 'RRY207',
                      'RRY208', 'RRY209', 'RRY210', 'RRY211', 'RRY212', 'RRY213', 'RRY214',
                      'RRY215', 'RRY216', 'RRY217', 'RRY218', 'RRY301', 'RRY302', 'RRY303',
                      'RRY304', 'RRY305', 'RRY306', 'RRY307', 'RRY308', 'RRY309', 'RRY310',
                      'RRY311', 'RRY312', 'RRY313', 'RRY314', 'RRY315', 'RRY316', 'RRY317',
                      'RRY318', 'RRY401', 'RRY402', 'RRY403', 'RRY404', 'RRY405', 'RRY406',
                      'RRY407', 'RRY408', 'RRY409', 'RRY410', 'RRY411', 'RRY412', 'RRY413',
                      'RRY414', 'RRY415', 'RRY416', 'RRY417', 'RRY501', 'RRY502', 'RRY503',
                      'RRY504', 'RRY505', 'RRY506', 'RRY507', 'RRY508', 'RRY509', 'RRY510',
                      'RRY511', 'RRY512', 'RRY513', 'RRY514', 'RRY515', 'RRY516', 'RRY601',
                      'RRY602', 'RRY603', 'RRY604', 'RRY605', 'RRY606', 'RRY607', 'RRY608',
                      'RRY609', 'RRY610', 'RRY611', 'RRY612', 'RRY613', 'RRY614', 'RRY615',
                      'RRY616', 'RRY617', 'RRY618']
        }, {
            "nomen": "rta",
            "nombre": "Tlalpan",
            "rutas": ['RTA101', 'RTA102', 'RTA103', 'RTA104', 'RTA105', 'RTA106', 'RTA107',
                      'RTA108', 'RTA109', 'RTA110', 'RTA111', 'RTA112', 'RTA113', 'RTA114',
                      'RTA115', 'RTA116', 'RTA117', 'RTA201', 'RTA202', 'RTA203', 'RTA204',
                      'RTA205', 'RTA206', 'RTA207', 'RTA208', 'RTA209', 'RTA210', 'RTA211',
                      'RTA212', 'RTA213', 'RTA214', 'RTA215', 'RTA216', 'RTA301', 'RTA302',
                      'RTA303', 'RTA304', 'RTA305', 'RTA306', 'RTA307', 'RTA308', 'RTA309',
                      'RTA310', 'RTA311', 'RTA312', 'RTA313', 'RTA314', 'RTA315', 'RTA316',
                      'RTA401', 'RTA402', 'RTA403', 'RTA404', 'RTA405', 'RTA406', 'RTA407',
                      'RTA408', 'RTA409', 'RTA410', 'RTA411', 'RTA412', 'RTA413', 'RTAM03',
                      'RTAM04', 'RTAM05', 'RTAM07', 'RTAM08', 'RTAM09', 'RTAO01']
        }, {
            "nomen": "v0r",
            "nombre": "Viga",
            "rutas": ['V0R001', 'V0R002', 'V0R003', 'V0R004', 'V0R005', 'V0R006', 'V0R007',
                      'V0R008', 'V0R009', 'V0R010', 'V0R011', 'V0R012', 'V0R013', 'V0R014',
                      'V0R015', 'V0R016', 'V0R017', 'V0R018', 'V0R019', 'V0R020', 'V0R021',
                      'V0R022', 'V0R023', 'V0R024', 'V0R025', 'V0R026', 'V0R027', 'V0R028',
                      'V0R029', 'V0R030', 'V0R031', 'V0R032', 'V0R033', 'V0R034', 'V0R035',
                      'V0R036', 'V0R037', 'V0R038', 'V0R039']
        }, {
            "nomen": "rza",
            "nombre": "Zaragoza",
            "rutas": ['RZAZ01', 'RZAZ02', 'RZAZ03', 'RZAZ04', 'RZAZ05', 'RZAZ06', 'RZAZ07',
                      'RZAZ08', 'RZAZ09', 'RZAZ10', 'RZAZ11', 'RZAZ12', 'RZAZ13', 'RZAZ14',
                      'RZAZ15', 'RZAZ16', 'RZAZ17', 'RZAZ18', 'RZAZ19', 'RZAZ20', 'RZAZ21',
                      'RZAZ22', 'RZAZ23', 'RZAZ24', 'RZAZ25', 'RZAZ26', 'RZAZ27', 'RZAZ28',
                      'RZAZ29', 'RZAZ30', 'RZAZ31', 'RZAZ32', 'RZAZ33', 'RZAZ34', 'RZAZ35',
                      'RZAZ36', 'RZAZ37', 'RZAZ38', 'RZAZ39', 'RZAZ40', 'RZAZ41', 'RZAZ42',
                      'RZAZ43', 'RZAZ44', 'RZAZ45', 'RZAZ46', 'RZAZ47', 'RZAZ48', 'RZAZ49',
                      'RZAZ50', 'RZAZ51', 'RZAZ52', 'RZAZ53', 'RZAZ54', 'RZAZ55', 'RZAZ56',
                      'RZAZ57', 'RZAZ58', 'RZAZ59', 'RZAZ60', 'RZAZ61', 'RZAZ62', 'RZAZ63',
                      'RZAZ64', 'RZAZ65', 'RZAZ66', 'RZAZ67', 'RZAZ68', 'RZAZ69', 'RZAZ70',
                      'RZAZ71', 'RZAZ72', 'RZAZ73', 'RZAZ74']
        }, {
            "nomen": "rcc",
            "nombre": "Coacalco",
            "rutas":  ['RCC100', 'RCC101', 'RCC102', 'RCC103', 'RCC104', 'RCC105', 'RCC106',
                       'RCC107', 'RCC108', 'RCC109', 'RCC110', 'RCC111', 'RCC112', 'RCC113',
                       'RCC114', 'RCC115', 'RCC116', 'RCC117', 'RCC200', 'RCC201', 'RCC202',
                       'RCC203', 'RCC204', 'RCC205', 'RCC206', 'RCC207', 'RCC208', 'RCC209',
                       'RCC210', 'RCC211', 'RCC212', 'RCC213', 'RCC214', 'RCC215', 'RCC216',
                       'RCC217', 'RCC300', 'RCC301', 'RCC302', 'RCC303', 'RCC304', 'RCC305',
                       'RCC306', 'RCC307', 'RCC308', 'RCC309', 'RCC310', 'RCC311', 'RCC312',
                       'RCC313', 'RCC314', 'RCC315', 'RCC316', 'RCC400', 'RCC401', 'RCC402',
                       'RCC403', 'RCC404', 'RCC405', 'RCC406', 'RCC407', 'RCC408', 'RCC409',
                       'RCC410', 'RCC411', 'RCC412', 'RCC413', 'RCC414', 'RCC415', 'RCC416',
                       'RCC417', 'RCC500', 'RCC501', 'RCC502', 'RCC503', 'RCC504', 'RCC505',
                       'RCC506', 'RCC507', 'RCC508', 'RCC509', 'RCC510', 'RCC511', 'RCC512',
                       'RCC513', 'RCC514', 'RCC515', 'RCC516', 'RCC517', 'RCC600', 'RCC601',
                       'RCC602', 'RCC603', 'RCC604', 'RCC605', 'RCC606', 'RCC607', 'RCC608',
                       'RCC609', 'RCC610', 'RCC611', 'RCC612', 'RCC613', 'RCC614', 'RCC615',
                       'RCC616', 'RCC617', 'RCC618', 'RCC619']
        }, {
            "nomen": "rcd",
            "nombre": "Cuautitlan",
            "rutas":  ['RCD701', 'RCD702', 'RCD703', 'RCD704', 'RCD705', 'RCD706', 'RCD707',
                       'RCD708', 'RCD709', 'RCD710', 'RCD711', 'RCD712', 'RCD713', 'RCD714',
                       'RCD715', 'RCD716', 'RCD717', 'RCD718', 'RCD719', 'RCD720', 'RCD721',
                       'RCD722', 'RCD723', 'RCD724', 'RCD725', 'RCD726', 'RCD727', 'RCD728',
                       'RCD729', 'RCD730', 'RCD731', 'RCD732', 'RCD733', 'RCD734', 'RCD735',
                       'RCD736', 'RCD737', 'RCD738', 'RCD739', 'RCD740', 'RCD741', 'RCD742',
                       'RCD743', 'RCD744', 'RCD745', 'RCD746', 'RCD747', 'RCD748', 'RCD749',
                       'RCD750', 'RCD751', 'RCD752', 'RCD753', 'RCD754', 'RCD755', 'RCD756',
                       'RCD757', 'RCD758', 'RCD759', 'RCD760', 'RCD761', 'RCD762', 'RCD763',
                       'RCD764', 'RCD765', 'RCD766', 'RCD767', 'RCD768', 'RCD769', 'RCD771',
                       'RCD772']
        },  {
            "nomen": "rpf",
            "nombre": "Pacifico",
            "rutas": {'PF0051', 'PF0052', 'RPF001', 'RPF002', 'RPF003', 'RPF004', 'RPF005',
                      'RPF006', 'RPF007', 'RPF008', 'RPF009', 'RPF010', 'RPF011', 'RPF012',
                      'RPF013', 'RPF014', 'RPF015', 'RPF016', 'RPF017', 'RPF018', 'RPF020',
                      'RPF021', 'RPF022', 'RPF023', 'RPF024', 'RPF026', 'RPF027', 'RPF028',
                      'RPF029', 'RPF031', 'RPF032', 'RPF033', 'RPF034', 'RPF035', 'RPF036',
                      'RPF037', 'RPF038', 'RPF039', 'RPF041', 'RPF042', 'RPF043', 'RPF044',
                      'RPF101', 'RPF102', 'RPF139', 'RPF141', 'RPF387', 'RPFT01'}
        },  {
            "nomen": "rte",
            "nombre": "Texcoco",
            "rutas": ['RTE100', 'RTE101', 'RTE102', 'RTE103', 'RTE104', 'RTE105', 'RTE106',
                      'RTE107', 'RTE108', 'RTE109', 'RTE110', 'RTE111', 'RTE112', 'RTE113',
                      'RTE114', 'RTE200', 'RTE201', 'RTE202', 'RTE203', 'RTE204', 'RTE205',
                      'RTE206', 'RTE207', 'RTE208', 'RTE209', 'RTE210', 'RTE211', 'RTE212',
                      'RTE213', 'RTE214', 'RTE300', 'RTE301', 'RTE302', 'RTE303', 'RTE304',
                      'RTE305', 'RTE306', 'RTE307', 'RTE308', 'RTE309', 'RTE310', 'RTE311',
                      'RTE312', 'RTE313', 'RTE314', 'RTE315', 'RTE400', 'RTE401']
        },  {
            "nomen": "rtl",
            "nombre": "Tlalnepantla",
            "rutas": ['RTL231', 'RTL232', 'RTL233', 'RTL234', 'RTL235', 'RTL236', 'RTL237',
                      'RTL238', 'RTL239', 'RTL240', 'RTL241', 'RTL242', 'RTL243', 'RTL244',
                      'RTL245', 'RTL246', 'RTL247', 'RTL248', 'RTL249', 'RTL250', 'RTL251',
                      'RTL252', 'RTL253', 'RTL254', 'RTL255', 'RTL256', 'RTL257', 'RTL258',
                      'RTL259', 'RTL260', 'RTL261', 'RTL262', 'RTL263', 'RTL264', 'RTL265',
                      'RTL266', 'RTL267', 'RTL268', 'RTL269', 'RTL270', 'RTL271', 'RTL272',
                      'RTL273', 'RTL274', 'RTL275', 'RTL276', 'RTL277', 'RTL278']
        }
    ]

    ftp = FTP('209.126.107.40')
    ftp.login(user='soportepointer', passwd='P01nt3r$')

    total_unidades_operativas = []

    for unidad_operativa in unidades_operativas:
        numero_rutas = len(unidad_operativa["rutas"])

        ftp.cwd(unidad_operativa["nomen"])
        files = []
        files = ftp.nlst()

        ruta_unica = []
        ruta_duplicada = []
        ruta_excedente = []

        file = []
        ruta = []
        rutaescenario = []
        escenario = []
        fechayhora = []
        anio = []
        mes = []
        dia = []
        hora = []
        minuto = []
        recargas = []
        faltante = []
        notifico = []

        # extrae fecha
        x = 0
        for linea in files:
            fechayhora.insert(x, linea[13:28])

            x += 1
            pass

        ahora = datetime.now().strftime("%Y%m%d_%H%M%S")
        ayer = datetime.now() - timedelta(days=1)
        ayer = ayer.strftime("%Y%m%d_180000")
        dia_semana = datetime.now().isoweekday()  # Lunes = 1

        # filtrar por fecha
        z = 0
        for linea in fechayhora:
            if linea > ayer:
                file.insert(z, files[z])
                pass
            z += 1
            pass

        # extraer datos
        y = 0
        for x in file:
            ruta.insert(y, x[0:6])
            rutaescenario.insert(y, x[0:12])
            escenario.insert(y, x[11:12])
            fechayhora.insert(y, x[13:28])
            anio.insert(y, x[13:17])
            mes.insert(y, x[17:19])
            dia.insert(y, x[19:21])
            hora.insert(y, x[22:24])
            minuto.insert(y, x[24:26])

            y += 1
            pass

        # comparar listas

        a = 0
        for line_r, line_e in zip(ruta, escenario):
            if line_r in unidad_operativa["rutas"]:
                if line_r in ruta_unica:
                    if line_e == '2':
                        recargas.append(line_r)
                    elif line_e == '1':
                        ruta_duplicada.insert(a, line_r)
                        pass
                elif line_e == '1':
                    ruta_unica.insert(a, line_r)
                elif line_e == '2':
                    recargas.append(line_r)
                    pass
            else:
                ruta_excedente.insert(a, line_r)
                pass
                a += 1
            pass

        for ruta in unidad_operativa["rutas"]:
            if ruta in ruta_unica:
                a = 1
            else:
                faltante.append(ruta)
                pass
            pass

        total_ruta_unica = len(ruta_unica)
        total_ruta_duplicada = len(ruta_duplicada)
        total_ruta_excedente = len(ruta_excedente)
        total_ruta_recarga = len(recargas)
        total_faltante = len(faltante)

        porcentaje = (total_ruta_unica * 100) / numero_rutas

        #		if porcentaje == 100:
        #			if unidad_operativa["conf_email"] == "si" :
        #				subject = 'Carga de archivos FTP -  '
        #				text_content = 'Se recibieron todos los archivos'
        #				html_content = '<h2>Coecillo</2><p><br>100</p>'
        #				from_email = '"origen" <soporte.dd.pointer@gmail.com>'
        #				to = 'soporte.dd.pointer@gmail.com'
        #				msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        #				msg.attach_alternative(html_content, "text/html")
        #				msg.send()
        #
        #				unidad_operativa["conf_email"]  = "no"
        #				pass
        #			pass



        total_unidad = {
            'numero_rutas': numero_rutas,
            "faltante": faltante,
            "total_faltante": total_faltante,
            "recargas": recargas,
            'total_recargas': total_ruta_recarga,
            "unica": total_ruta_unica,
            "excedente": ruta_excedente,
            "total_excedente": total_ruta_excedente,
            "duplicada": ruta_duplicada,
            "total_duplicada": total_ruta_duplicada,
            'porcentaje': porcentaje,
            'nombre': unidad_operativa["nombre"],
            'nomen': unidad_operativa["nomen"],
            'notifico': notifico,
        }

        total_unidades_operativas.append(total_unidad)

        ftp.cwd("..")

    ftp.quit()

    notificar = "no"

    if notificar == "si":
        subject = 'Carga de archivos FTP -  '
        text_content = 'Se recibieron todos los archivos'
        html_content = '<h2>Coecillo</2><p><br>100</p>'
        from_email = '"origen" <soporte.dd.pointer@gmail.com>'
        to = 'soporte.dd.pointer@gmail.com'
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
    pass

    context = {
        'titulo': titulo,
        'total_unidades_operativas': total_unidades_operativas,
    }

    return HttpResponse(template.render(context, request))


def wsns(request):
    template = loader.get_template('cargafiles/wsns.html')
    titulo = 'WebServices neosoft'


    ruta = []
    rutaescenario = []
    escenario = []
    fechayhora = []
    anio = []
    mes = []
    dia = []
    hora = []
    minuto = []
    nombre = []


    r = requests.post('http://controlcenterm2m.com/fleetapi/center/cargafiles', data={
        'api_login': '0366d1cb254ae139',
        'api_key': '2362c286ad0acae8cc253260548cb9fa',
        'from_date': '2017-05-15',
        'to_date': '2017-05-15',
    })
    response = r.json()

    if response['status'] == True:
        for page in response['data']:
            nombre.append(page['nam'])
            pass
        # extraer datos
        y = 0
        for x in nombre:
            ruta.insert(y, x[0:6])
            rutaescenario.insert(y, x[0:12])
            escenario.insert(y, x[11:12])
            fechayhora.insert(y, x[13:28])
            anio.insert(y, x[13:17])
            mes.insert(y, x[17:19])
            dia.insert(y, x[19:21])
            hora.insert(y, x[22:24])
            minuto.insert(y, x[24:26])

            y += 1
            pass

    context = {
        'titulo': titulo,
        'response': response,
        'nombre': nombre,
        'ruta': ruta,
    }

    return HttpResponse(template.render(context, request))
