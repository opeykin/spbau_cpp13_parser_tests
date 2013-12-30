TEST_DIR=tests
SOURCE_DIR=$TEST_DIR/source
FAILED_DIR=$TEST_DIR/failed
OUTPUT_DIR=$TEST_DIR/output
CORRECT_OUTPUT_DIR=$TEST_DIR/correct_output

for FNAME in $(ls $FAILED_DIR); do
	echo $FNAME
	echo "------------------------correct------------------"
	cat $CORRECT_OUTPUT_DIR/$FNAME
	echo "------------------------output-------------------"
	cat $OUTPUT_DIR/$FNAME
	echo
done
