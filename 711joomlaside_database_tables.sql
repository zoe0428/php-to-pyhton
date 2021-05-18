CREATE TABLE customer_login(
  customer_id INT UNSIGNED AUTO_INCREMENT NOT NULL COMMENT 'Customer unique id',
  login_name VARCHAR(20) NOT NULL COMMENT 'login user name',
  password CHAR(32) NOT NULL COMMENT 'pwd hashed by DM5',
  user_stats TINYINT NOT NULL DEFAULT 1 COMMENT 'user stats',
  PRIMARY KEY (customer_id)
) ENGINE = innodb COMMENT 'customer login table'


CREATE TABLE customer_inf(
  customer_inf_id INT UNSIGNED AUTO_INCREMENT NOT NULL COMMENT 'customer id',
  customer_id INT UNSIGNED NOT NULL COMMENT 'customer_login id foreign key ',
  customer_last_name VARCHAR(20) NOT NULL COMMENT 'user last name',
  customer_first_name VARCHAR(20) NOT NULL COMMENT 'user first name',
  mobile_phone INT UNSIGNED COMMENT 'phone number',
  customer_email VARCHAR(50) COMMENT 'email address',
  gender CHAR(1) COMMENT 'gender: M-male. F-female ',
  register_time TIMESTAMP NOT NULL COMMENT 're',
  user_money DECIMAL(8,2) NOT NULL DEFAULT 0.00 COMMENT 'account amount',
  modified_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'last modified_time',
  PRIMARY KEY (customer_inf_id),
  FOREIGN KEY(customer_id) references customer_login(customer_id)
) ENGINE = innodb COMMENT 'customer info table';


CREATE TABLE customer_balance_log(
  balance_id INT UNSIGNED NOT NULL AUTO_INCREMENT COMMENT 'balance ID',
  customer_id INT UNSIGNED NOT NULL COMMENT 'customer_login ID',
  source TINYINT UNSIGNED NOT NULL DEFAULT 1 COMMENT 'record change source : 1 create order. 2  refund',
  source_sn INT UNSIGNED NOT NULL COMMENT 'order_sn ID',
  create_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'log happen time',
  amount DECIMAL(8,2) NOT NULL DEFAULT 0.00 COMMENT 'amount change ',
  PRIMARY KEY （balance_id),
  FOREIGN KEY  (customer_id) references customer_login(customer_id)
) ENGINE = innodb COMMENT 'balance change log';

CREATE TABLE product_info(
  product_id INT UNSIGNED AUTO_INCREMENT NOT NULL COMMENT 'product ID',
  product_core CHAR(16) NOT NULL COMMENT 'product unique code',
  product_name VARCHAR(20) NOT NULL COMMENT 'product name',
  price DECIMAL(8,2) NOT NULL COMMENT 'product price',
  publish_status TINYINT(3) NOT NULL DEFAULT 0 COMMENT 'product status：0 empty 1 on load',
  audit_status TINYINT(3) NOT NULL DEFAULT 0 COMMENT 'check status：0 yes，1 no',
  descript TEXT NOT NULL COMMENT 'product descript',
  modified_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'last modified_time',
  PRIMARY KEY (product_id)
) ENGINE = innodb COMMENT 'prodect as service table';

CREATE TABLE product_result(
  result_id INT UNSIGNED AUTO_INCREMENT NOT NULL COMMENT 'result ID',
  product_id INT UNSIGNED  NOT NULL COMMENT 'product ID',
  data_url TEXT NOT NULL COMMENT 'customer upload file address',
  result_url TEXT NOT NULL COMMENT ' prediciton result file address',
  result_status TINYINT(3) NOT NULL DEFAULT 0 COMMENT '0 on process, 1 prediciton compelet',
  modified_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'last modified_time',
  PRIMARY KEY (product_id),
  FOREIGN KEY (product_id) references product_info(product_id)
) ENGINE = innodb COMMENT 'prodect as service table';

CREATE TABLE order_master(
  order_id INT UNSIGNED NOT NULL AUTO_INCREMENT COMMENT 'ID',
  order_sn BIGINT UNSIGNED NOT NULL COMMENT 'order number: yyyymmddnnnnnnnn',
  customer_id INT UNSIGNED NOT NULL COMMENT 'order customer ID',
  payment_method TINYINT(4) NOT NULL COMMENT 'method：1 paypal，2 visa，3 mastercard，4 bank transcription',
  order_money DECIMAL(8,2) NOT NULL COMMENT 'ordre amount',
  payment_money DECIMAL(8,2) NOT NULL DEFAULT 0.00 COMMENT 'paid money',
  create_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'order create time',
  pay_time DATETIME COMMENT 'order pay time',
  finnish_time DATETIME COMMENT 'order compelte'
  order_status TINYINT(3) NOT NULL DEFAULT 0 COMMENT 'order status: 0 on process, 1 compelet, 2 delete',
  modified_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'last modified_time',
  PRIMARY KEY (order_id),
  FOREIGN KEY (customer_id) references customer_login(customer_id)

)ENGINE = innodb COMMENT 'order main table';

CREATE TABLE order_detail(
  order_detail_id INT UNSIGNED NOT NULL AUTO_INCREMENT COMMENT 'order detial ID',
  order_id INT UNSIGNED NOT NULL COMMENT 'order ID',
  product_id INT UNSIGNED NOT NULL COMMENT 'product ID',
  result_id INT UNSIGNED NOT NULL COMMENT 'result ID',
  product_name VARCHAR(50) NOT NULL COMMENT 'service name',
  product_price DECIMAL(8,2) NOT NULL COMMENT 'service price',
  modified_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'last modified_time',
  PRIMARY KEY pk_orderdetailid(order_detail_id),
  FOREIGN KEY (order_id) references order_master(order_id),
  FOREIGN KEY (product_id) references product_info(product_id),
  FOREIGN KEY (result_id) references product_result(result_id)
)ENGINE = innodb COMMENT 'order_detail' 