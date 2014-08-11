OUTPUTS = autotab.plugin  autotab.py determine.py
DESTDIR = ~/.local/share/gedit/plugins

install: autotab.plugin  autotab.py determine.py
	@ [ `whoami` != "root" ] || ( echo 'Run make install as yourself, not as root.' ; exit 1 )
	mkdir -p $(DESTDIR)
	cp $(OUTPUTS) $(DESTDIR)

uninstall:
	rm -f $(foreach o, $(OUTPUTS), $(DESTDIR)/$o)

