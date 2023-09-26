bit :
	xsdb bit.tcl
download_driver :
	insmod ./driver/open-nic-driver/onic.ko

compile-driver :
	make -C ./driver/

compile-hwtestlib :
	make -C ./hwtestlib/ libsume
	cp ./hwtestlib/libsume.so ./app/
update :
	python3 ./app/write_hash_entropy.py
	python3 ./app/write_hash_pcsa.py
	python3 ./app/write_hash_ams.py
	python3 ./app/write_table.py
read :
	python3 ./app/dashboard.py
clean :
	make -C ./driver/ clean
	make -C ./hwtestlib/ clean
	rm -f ./app/libsume.so
