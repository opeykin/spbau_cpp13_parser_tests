PATH_TO_TESTS=/home/alex/study/cpp/parser/spbau_cpp13_parser_tests/tests
TEST_DIR=tests
SOURCE_DIR=$TEST_DIR/source
FAILED_DIR=$TEST_DIR/failed
INPUT_DIR=$TEST_DIR/input
OUTPUT_DIR=$TEST_DIR/output
CORRECT_OUTPUT_DIR=$TEST_DIR/correct_output
PP=bin/pp

green='\e[0;32m'
red='\e[0;31m'
endColor='\e[0m'

rm -rf $TEST_DIR
cp -r $PATH_TO_TESTS $TEST_DIR
mkdir $FAILED_DIR
mkdir $OUTPUT_DIR

for FNAME in $(ls $SOURCE_DIR); do
	echo -n "$FNAME: "
	
	cat $INPUT_DIR/$FNAME | $PP $SOURCE_DIR/$FNAME > $OUTPUT_DIR/$FNAME 2>&1

	if ! diff -q $OUTPUT_DIR/$FNAME $CORRECT_OUTPUT_DIR/$FNAME > /dev/null ; then
		echo -e "${red}[FAIL]${endColor}"
		touch $FAILED_DIR/$FNAME
	else
		echo -e "${green}[PASS]${endColor}"
	fi
done
