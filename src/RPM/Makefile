NAME=$(shell cut -d - -f 1 ../VERSION)
PKG_NAME=$(shell cat ../VERSION)
SPEC=$(NAME).spec
SPEC_LINK=$(NAME)-link.spec
RPMBUILD=rpmbuild

TARGET=$(shell ../config.guess)
RPM_FLAGS --target=$(TARGET)

rpm: ../$(PKG_NAME).tar.gz $(SPEC)
	$(RPMBUILD) -bb $(RPM_FLAGS) $(SPEC)

$(SPEC): initial.spec ../VERSION
	./build_spec_file

rpm-link: $(SPEC_LINK)
	$(RPMBUILD) -bb $(RPM_FLAGS) $(SPEC_LINK)

$(SPEC_LINK): initial.spec ../VERSION
	./build_spec_file link


srpm: ../$(PKG_NAME).tar.gz $(SPEC)
	$(RPMBUILD) -bs $(SPEC)


../$(PKG_NAME).tar.gz:
	(cd ..; make dist)
	-rm $(SPEC)


clean:
	-rm $(NAME)*.spec



rpm_env:
	$(RPMBUILD) $(RPM_FLAGS) -bp rpm_env.spec >/dev/null 2>&1


NAMES_FILE=/tmp/rpm_names

names: rpm_env
	@echo '# file generated by src/RPM/Makefile' >$(NAMES_FILE)
	@(. /tmp/rpm_env; \
	echo RPM=$$RPM_RPMS_DIR/$$ARCH/$(PKG_NAME)-1.$$ARCH.rpm >>$(NAMES_FILE); \
	echo SRPM=$$RPM_SRPMS_DIR/$(PKG_NAME)-1.src.rpm >>$(NAMES_FILE))


