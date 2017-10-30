#! /bin/bash
# original script by J. Simone

singularity exec /data/simone/singularity/ubuntu16-cuda8-cudnn6-ml.img /bin/bash <<EOF
cat /etc/issue
nvidia-smi
source /.singularity.d/environment
python <<XEOF
import tensorflow as tf
# Creates a graph.
with tf.device('/gpu:0'):
  a = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[2, 3], name='a')
  b = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[3, 2], name='b')
  c = tf.matmul(a, b)
# Creates a session with log_device_placement set to True.
sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))
# Runs the op.
print(sess.run(c))
XEOF
EOF
