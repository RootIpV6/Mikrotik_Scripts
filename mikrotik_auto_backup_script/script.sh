
/export file=config;
/system backup save name=config;
/tool e-mail send to="BACKUP'ın GÖNDERİLECEĞİ MAİL ADRESİNİ YAZINIZ" subject=([/system identity get name]." Backup") body=("Mikrotik Configuration Backup for - ".[/system clock get date]) file=config.rsc,config.backup;
/log info "Backup e-mail sent.";


Mikrotik/AUTOBACKUP SCRİPT
System/Script section.
/export file=config;
/system backup save name=config;
/tool e-mail send to="THE E-MAIL ADDRESS TO WHICH THE BACKUP WILL BE SENT MUST BE WRITTEN." subject=([/system identity get name]." Backup") body=("Mikrotik Configuration Backup for - ".[/system clock get date]) file=config.rsc,config.backup;
/log info "Backup e-mail sent.";
