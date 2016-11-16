# import subprocess
# lpr = subprocess.Popen("C:/Users/acarrillo/Desktop/pap.pdf", stdin=subprocess.PIPE)
# lpr.stdin.write(your_data_here)

import os
from django.http import HttpResponse
import os, sys
import win32print
import win32api

from reportes_models import *
from reportes_models import *
import cgi
import tempfile
import tempfile
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch

import win32com.client
import os.path

#
# def imprimir(request):
#
#     lista = []
#     #
#     # lista.append(1)
#     #
#     # os.startfile("C:/Users/acarrillo/Desktop/pap.pdf", "print")
#
#
#     filename = tempfile.mktemp(".txt")
#     open(filename, "w").write("This is a test")
#     win32api.ShellExecute(
#         0,
#         "print",
#         filename,
#         #
#         # If this is None, the default printer will
#         # be used anyway.
#         #
#         '/d:"%s"' % win32print.GetDefaultPrinter(),
#         ".",
#         0
#     )
#
#     win32api.ShellExecute(0, "print", pdf_file_name, None, ".", 0)
#
#     HttpResponse(lista)

# def imprimir(request):
#
#     lista = []
#     #
#     # lista.append(1)
#     #
#     # os.startfile("C:/Users/acarrillo/Desktop/pap.pdf", "print")
#
#
#
#     printer_name = win32print.GetDefaultPrinter()
#     #
#     # raw_data could equally be raw PCL/PS read from
#     #  some print-to-file operation
#     #
#     if sys.version_info >= (3,):
#         raw_data = bytes("This is a test", "utf-8")
#     else:
#         raw_data = "This is a test"
#
#     hPrinter = win32print.OpenPrinter(printer_name)
#
#     try:
#         hJob = win32print.StartDocPrinter(hPrinter, 1, ("test of raw data", None, "RAW"))
#         try:
#             win32print.StartPagePrinter(hPrinter)
#             win32print.WritePrinter(hPrinter, raw_data)
#             win32print.EndPagePrinter(hPrinter)
#         finally:
#             win32print.EndDocPrinter(hPrinter)
#     finally:
#         win32print.ClosePrinter(hPrinter)
#
#     return HttpResponse(lista)



# def imprimir(request):
#
#     lista = []
#
#     filename = tempfile.mktemp ("C:/Users/acarrillo/Desktop/pap.pdf")
#     open(filename, "w").write ("This is a test")
#     win32api.ShellExecute(
#       0,
#       "printto",
#       filename,
#       '"%s"' % win32print.GetDefaultPrinter (),
#       ".",
#       0
#     )
#
#     return HttpResponse(lista)


#
# def imprimir(request):
#
#     lista = []
#
#     source_file_name = "C:/Users/acarrillo/Desktop/test.txt"
#     pdf_file_name = tempfile.mktemp(".pdf")
#
#     styles = getSampleStyleSheet()
#     h1 = styles["h1"]
#     normal = styles["Normal"]
#
#     doc = SimpleDocTemplate(pdf_file_name)
#     #
#     # reportlab expects to see XML-compliant
#     #  data; need to escape ampersands &c.
#     #
#     text = cgi.escape(open(source_file_name).read().decode('latin-1')).splitlines()
#
#     #
#     # Take the first line of the document as a
#     #  header; the rest are treated as body text.
#     #
#     story = [Paragraph(text[0], h1)]
#     for line in text[1:]:
#         story.append(Paragraph(line, normal))
#         story.append(Spacer(1, 0.2 * inch))
#
#     doc.build(story)
#     win32api.ShellExecute(0, "print", pdf_file_name, None, ".", 0)
#
#     return HttpResponse(lista)


def imprimir(request):
    lista = []
    lista_distrito = []

    # lista_distrito.append('020801')
    lista_distrito.append('020601')
    # lista_distrito.append('021509')
    # lista_distrito.append('021806')
    # lista_distrito.append('022001')
    # lista_distrito.append('030212')
    # lista_distrito.append('030602')
    # lista_distrito.append('050507')
    # lista_distrito.append('050601')
    # lista_distrito.append('050617')
    # lista_distrito.append('060903')
    # lista_distrito.append('080301')
    # lista_distrito.append('080205')
    # lista_distrito.append('080206')
    # lista_distrito.append('080207')
    # lista_distrito.append('080402')
    # lista_distrito.append('080407')
    # lista_distrito.append('090203')
    # lista_distrito.append('090208')
    # lista_distrito.append('090301')
    # lista_distrito.append('110107')
    # lista_distrito.append('110204')
    # lista_distrito.append('120201')
    # lista_distrito.append('120501')
    # # lista_distrito.append('120708')
    # lista_distrito.append('130202')
    # lista_distrito.append('131203')
    # lista_distrito.append('130701')
    # # lista_distrito.append('130705')
    # lista_distrito.append('131203')
    # lista_distrito.append('140107')
    # lista_distrito.append('150116')
    # lista_distrito.append('150508')
    # lista_distrito.append('150604')
    # lista_distrito.append('150705')
    # lista_distrito.append('170102')
    # lista_distrito.append('180106')
    #
    # lista_distrito.append('180208')
    # lista_distrito.append('180210')
    # lista_distrito.append('190111')
    # lista_distrito.append('180210')
    #
    # lista_distrito.append('210407')
    # lista_distrito.append('230106')
    # lista_distrito.append('230109')
    # lista_distrito.append('240103')
    # lista_distrito.append('240105')
    # lista_distrito.append('240106')
    lista = []
    lista_zonas = []

    for ubigeos in lista_distrito:
        #tempprinter = "\\\\server01\\printer01"
        # tempprinter = "\\\\172.18.1.35\\192.168.230.68"
        # total_zonas = int(str(Esp_Aeus.objects.filter(ubigeo=lista_distrito[ubigeos]).values_list('zona', flat=True).distinct().count()))
        total_zonales = Esp_Aeus.objects.filter(ubigeo=ubigeos).values_list('zona', flat=True)
        cuchi_zona = list(set(total_zonales))

        #lista_zonas.append(total_zonas)

        for zona_t in cuchi_zona:
            # zoner = str(zona_t+1).zfill(3)+"00"
            # total_aes_zona = int(str(Esp_Aeus.objects.filter(ubigeo=lista_distrito[ubigeos], zona=zona_t).count()))
            # total_secc_zona= Esp_Aeus.objects.filter(ubigeo=ubigeos, zona=zona_t).values_list('seccion', flat=True)
            total_secc_zona = Esp_Aeus.objects.filter(ubigeo=ubigeos, zona=zona_t).values_list('seccion', flat=True)
            cuchi_seccion = list(set(total_secc_zona))

            print "SeccioneS: ->"

            for secci in cuchi_seccion:
                #total_secc_ae = int(str(Esp_Aeus.objects.filter(ubigeo=ubigeos, zona='00600', seccion=secci).count()))
                total_secc_zona = Esp_Aeus.objects.filter(ubigeo=ubigeos, zona=zona_t, seccion=secci).values_list('aeu_final', flat=True)
                cuchi_aeu = list(set(total_secc_zona))
                # list.append(aeu+1)
                for aeu in cuchi_aeu:
                    lista.append(str(ubigeos)+" : "+zona_t + ", "+str(secci)+", "+str(aeu) + "<br/>")
                    # str(zona_t + 1)+": " + str(aeu + 1) + "<br/>"
                    sacar_impresion(request, str(ubigeos), zona_t, str(secci), str(aeu))

    return HttpResponse(lista)

def sacar_impresion(request,ubigeo, zonaq, seccq, aeut):

    lista =[]
    lista.append(str(ubigeo)+": " +str(zonaq) +",  "+ str(seccq)+","+str(aeut) +"<br/>")


    #cond = Esp_Aeus.objects.filter(ubigeo=ubigeo, zona=zonaq, aeu_final=aeut)
    tempprinter = "\\\\172.18.1.35\\192.168.230.16"
    currentprinter = win32print.GetDefaultPrinter()


    secc = str(seccq).zfill(3)
    aeu_conv = str(aeut).zfill(3)
    #surce_file_name = "C:/Users/acarrillo/Desktop/pap.pdf"
    print ubigeo
    print zonaq
    print seccq
    print aeu_conv
    source_file_name = "\\\srv-fileserver\\CPV2017\\list_segm_esp\\"+str(ubigeo)+"\\"+str(zonaq)+"\\"+str(ubigeo)+str(zonaq)+str(secc)+str(aeu_conv)+".pdf"
    print source_file_name
    # \\\srv - fileserver\\CPV2017\\list_segm_esp\\" + str(ubigeo) + "\\" + zonal + "\\" + str(ubigeo) + zonal + str(secc) + str(aeu_conv) + ".pdf"

    win32print.SetDefaultPrinter(tempprinter)
    win32api.ShellExecute(0, "print", source_file_name, None, ".", 0)
    win32print.SetDefaultPrinter(currentprinter)

    return HttpResponse(lista)

# # tempprinter = "\\\\server01\\printer01"
# # tempprinter = "\\\\172.18.1.35\\192.168.230.68"
# tempprinter = "\\\\172.18.1.35\\192.168.230.16"
# currentprinter = win32print.GetDefaultPrinter()
# source_file_name = "C:/Users/acarrillo/Desktop/pap.pdf"
# win32print.SetDefaultPrinter(tempprinter)
# win32api.ShellExecute(0, "print", source_file_name, None, ".", 0)
# win32print.SetDefaultPrinter(currentprinter)