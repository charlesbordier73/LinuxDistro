#!/bin/sh
  
  cp $BASE_DIR/../custom-scripts/S41network-config $BASE_DIR/target/etc/init.d
  chmod +x $BASE_DIR/target/etc/init.d/S41network-config

  mkdir -p $BASE_DIR/target/home/charles/t1
  chmod +x $BASE_DIR/target/etc/init.d/t1.py
  cp $BASE_DIR/../custom-scripts/t1.py-config $BASE_DIR/target/etc/init.d
