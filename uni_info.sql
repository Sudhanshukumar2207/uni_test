CREATE TABLE `sign_up` (
  `sn` int NOT NULL AUTO_INCREMENT,
  `un` varchar(1000) DEFAULT NULL,
  `uid` varchar(1000) DEFAULT NULL,
  `pw` varchar(1000) DEFAULT NULL,
  `sq` varchar(1000) DEFAULT NULL,
  `sa` varchar(1000) DEFAULT NULL,
  `role` varchar(145) DEFAULT NULL,
  `status` varchar(145) DEFAULT NULL,
  PRIMARY KEY (`sn`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci



CREATE TABLE `university_info` (
  `u_name` varchar(1000) NOT NULL,
  `mode` varchar(1000) NOT NULL,
  `u_reg` varchar(2000) NOT NULL,
  `link` varchar(150) NOT NULL,
  `broch` longblob,
  `pors` longblob,
  `a_f` longblob
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci




CREATE TABLE `program_details` (
  `u_name` varchar(150) NOT NULL,
  `mode` varchar(150) NOT NULL,
  `p_name` varchar(150) NOT NULL,
  `lateral_Entry` varchar(150) DEFAULT NULL,
  `min_dur` varchar(150) NOT NULL,
  `max_dur` varchar(150) NOT NULL,
  `eligibility` varchar(200) NOT NULL,
  `session` varchar(150) NOT NULL,
  `pro_fees` varchar(150) NOT NULL,
  `adm_fees` varchar(150) NOT NULL,
  `exam_fees` varchar(150) NOT NULL,
  `ser_fees` varchar(150) NOT NULL,
  `ref_fees` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci