import operator
from textwrap import wrap

def ceas2(text, shift):
    result = ""
    text = text.upper()

    for i in range(len(text)):
        char = text[i]
        # Encrypt uppercase characters in plain text
        if char in "qwertyuiopasdfghjklzxcvbnm".upper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        else:
            result += char

    return result


def vin(txt, keyword):
    lenk = len(keyword)
    result = ""
    txt = txt.replace(" ", "")
    lstxt = wrap(txt,lenk)

    for chunk in lstxt:
        for i in keyword:
            shift = -(ord(i) - 65)
            char = chunk[keyword.index(i)]
            r = ceas2(char, shift)
            result = result + r
            print(char, r, shift)


    return result


def originalText(cipher_text, key): 
    orig_text = [] 
    for i in range(len(cipher_text)): 
        x = (ord(cipher_text[i]) - 
             ord(key[i]) + 26) % 26
        x += ord('A') 
        orig_text.append(chr(x)) 
    return("" . join(orig_text)) 
#Advanced Security 1 –DT211-4, DT282-4 and DT228-4
#Lab Sheet 2

#1. The following information was encrypted using Caesar Cipher. Decrypt it. 
#Ans: 3
txt = "RQH  YDULDWLRQ  WR  WKH  VWDQGDUG  FDHVDU  FLSKHU  LV  ZKHQ WKH    DOSKDEHW    LV    NHBHG    EB    XVLQJ    D    ZRUG.    LQ    WKH WUDGLWLRQDO  YDULHWB,  RQH  FRXOG  ZULWH  WKH  DOSKDEHW  RQ WZR  VWULSV  DQG  MXVW  PDWFK  XS  WKH  VWULSV  DIWHU  VOLGLQJ WKH  ERWWRP  VWULS  WRWKH  OHIW  RU  ULJKW.  WR  HQFRGH,  BRX ZRXOG  ILQG  D  OHWWHU  LQ  WKH  WRS  URZ  DQG  VXEVWLWXWH  LW IRU  WKH  OHWWHU  LQ  WKH  ERWWRP  URZ.  IRU  D  NHBHG  YHUVLRQ, RQH ZRXOG QRW XVH D VWDQGDUG DOSKDEHW, EXW ZRXOG ILUVW ZULWH  D  ZRUG  (RPLWWLQJ  GXSOLFDWHG  OHWWHUV)  DQG  WKHQ ZULWH WKH  UHPDLQLQJ  OHWWHUV  RI  WKH  DOSKDEHW.  IRU  WKH HADPSOH EHORZ, L XVHG D NHB RI UXPNLQ.FRP DQG BRX ZLOO VHH WKDW WKH SHULRG LV UHPRYHG EHFDXVH LW LV QRW D OHWWHU. BRX   ZLOO   DOVR   QRWLFH   WKH   VHFRQG   P   LV   QRW   LQFOXGHG EHFDXVH   WKHUH   ZDV   DQ   P   DOUHDGB   DQG   BRX   FDQ'W   KDYH GXSOLFDWHV."
out = ceas2(txt, -3)
print("Q1", "", out)
print("----------------------------------------------------------------------------")
print("----------------------------------------------------------------------------")

#2. Find the key which was used to encrypt this messageusing Caesar Cipher.  
#Ans: -17
print("Q2")
txt = "FEV  MRIZRKZFE   KF  KYV  JKREURIU  TRVJRI  TZGYVI   ZJ  NYVE  KYV RCGYRSVK   ZJ   BVPVU   SP   LJZEX   R   NFIU.   ZE   KYV   KIRUZKZFERC MRIZVKP,  FEV TFLCU NIZKV KYV RCGYRSVK FE KNF JKIZGJ REU ALJK DRKTY  LG  KYV  JKIZGJ  RWKVI  JCZUZEX  KYV  SFKKFD  JKIZG  KF  KYV CVWK FI  IZXYK. KF  VETFUV, PFL  NFLCU  WZEU R CVKKVI  ZE  KYV KFG IFN  REU  JLSJKZKLKV  ZK  WFI  KYV  CVKKVI  ZE  KYV  SFKKFD  IFN.  WFI  R BVPVU  MVIJZFE,  FEV  NFLCU  EFK  LJV  R  JKREURIU  RCGYRSVK,  SLK NFLCU  WZIJK  NIZKV  R  NFIU  (FDZKKZEX  ULGCZTRKVU  CVKKVIJ)  REU KYVE  NIZKV  KYV  IVDRZEZEX  CVKKVIJ  FW  KYV  RCGYRSVK.  WFI  KYV VORDGCV  SVCFN,  Z  LJVU  R  BVP  FW  ILDBZE.TFD  REU  PFL  NZCC  JVV KYRK  KYV  GVIZFU  ZJ  IVDFMVU  SVTRLJV  ZK  ZJ  EFK  R  CVKKVI.  PFL NZCC RCJF EFKZTV KYV JVTFEU D ZJ EFK ZETCLUVU SVTRLJV KYVIV NRJ RE D RCIVRUP REU PFL TRE'K YRMV ULGCZTRKVJ."

for i in range(-26, 0):
    out2 = ceas2(txt, i)
    print("----------------------------------------------------------------------------")
    print(i, out2)

#3. The following message has been encrypted using Vinegeré Cipher with a keyword KISWAHILI. Decrypt the message.
#Ans: 
print("----------------------------------------------------------------------------")
print("----------------------------------------------------------------------------")

txt= "XQKP  IZ  IMWEB  LK  AUVZCXKW  PHL  VPE  RIKD  ASOZZSBZI  TOIE  ESTD XEJWXM CPS-3. PHPA TA DPW NEZCWB YN S OIE-GPIB KGIPLBTBSWF, WNK UJ  WGV  KGEPV  TA  YVW  KF  APP  NSDW  NETITVSVY  BIUIWQCBK  (KUA  WQ IX QFETPIW 64). QD'A HNOIIMTI BGK LHBP NYZ EA TV IQNOKL PHL NTVKT VACPATWX, JMP I HU SWZQFC FVZ YW KESND. PB'D VYB LDAA BSM XMODAZP QCXKLEOUA LZOV'L WNF OZWN, QL'O TOIE EO LGJ'T YMLTVG FAEK WYM. GPWJ WL AEIBBWZ TOQD XBWUASZ JLKU QF 2006, ET SWZSOL SO IM EP   EYCDZ   BL   VPMNQFC   A   UMH   PKAZ   BUUKEQYV   KKOU.   BSM   CPS BATQWG  (GPAYH  PA  CMKTDU  PHZE  WP  BZA  MK4  IYL  WL5  XWMPTJ),  EKA MJDLZ TVMZWWSPVR XBMKOUYM QZYU FAW AGAMC WX YRFXEIXIDUSPA.   HM   NQVJ'T   RVZE   RWO   HOUO   EPO   DSNIVCD   ARI-2 NWRPIYBC  EGQLK  ZPUKQF  OEJCCM.  LCL  ET'Z  2012,  IYL  CPS-512  ES  ZBTTV TGKKPVR OYWV.AVLV  HWBAW,  JOUM  ZN  DPW  OHH-3  KLVNQVWTLA  TA  CQYJIMQNIXBDU BLBEMB.  AGIE  HZP  NKALAR,  ICE VYB  GNDLZD  WP  USCNPBFLO  NSOTLZ. DWWM  SNE  ZULTVMJ  EN  OICLGIJA,  BBB  YWD  WJZEYA  ZN  WIYJIACOM CUSHLLZ.  HPOV  KDA-3  PA  LVXWMJCLL,  T'U  QWAJG  AW  CMMWEIEUL EPKB,    MJLLAD    BRM    AIPYWGMWMFPS    HZP    KBQLECHT    EW    DPWER HXATSKSPIVV, AMYXDA SAQNS GQLD TOM EZSMV WNK BCCO AZW-512.AATPICB  XKR  H  ESQVM.  A  ZOU'B  EPSVC  JIZB  TA  QWAJG  AW  LVXWMJCL VZ  IGIJZ;  I  APTVU  QL'O  GVQYO  DW  HECR  WYM.  KVV  KF  APP  NSDW NETITVSVY,  E  DVV'E  ZOIDHY  OIGM  K  NSROYQEM.  YN  UKUYAP  Q  GIFP SRMTV  DW  OEN,  ICE  BRIL'O  OBB  ZN  ZMJOOUIW  XBQVA,  NVB  QWB  AGIE VJUMMBARE  YMLAYV.  SJD  DPTTO  Q  DEKL  AZUO  UGNE  APLV  YBZARZ,  Q EPSVC  WNF  EZCVL  TA  ORIJ.  EOTD,  IAFJP  BRMJA'S  VVP  ZOIKKN  UQDB CPGQLK  KSWYAW  OKLQY.  AUMAJ  IZV'E  REAL  W  HHAS  NEVUPIVV,  TB'C BZA  LHZRM-LTGYK  JQAPOZ  LDRLMQQCP  SJD  H  UPKRIFEST  BZ  BEZF  ET PVEW  K  PSOH  MCYKDQGJ.  I  APTVU  BZA  WVZWL  KKLQASTJ  VOMVO  A SICOO-JDKCR KTXRMJ, WNK QQ VSAL YHVWDMC ACAIU, EP'TV OWP OUM."
key = "KISWAHILI"
out3 = originalText(txt, key)
print("Q3", wrap(out3, 8))
print("----------------------------------------------------------------------------")
