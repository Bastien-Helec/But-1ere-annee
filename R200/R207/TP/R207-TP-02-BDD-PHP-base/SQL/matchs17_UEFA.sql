-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Feb 07, 2023 at 03:50 PM
-- Server version: 10.6.11-MariaDB
-- PHP Version: 7.4.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `footdb`
--

-- --------------------------------------------------------

--
-- Table structure for table `matchs17_UEFA`
--

CREATE TABLE `matchs17_UEFA` (
  `id` int(11) UNSIGNED NOT NULL,
  `eq1` int(10) DEFAULT NULL,
  `score1` int(4) DEFAULT NULL,
  `eq2` int(10) DEFAULT NULL,
  `score2` int(4) DEFAULT NULL,
  `dateMatch` date DEFAULT NULL,
  `journee` int(3) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `matchs17_UEFA`
--

INSERT INTO `matchs17_UEFA` (`id`, `eq1`, `score1`, `eq2`, `score2`, `dateMatch`, `journee`) VALUES
(1, 1, 1, 2, 2, '2017-09-12', NULL),
(2, 3, 3, 4, 0, '2017-09-12', NULL),
(3, 4, 5, 1, 0, '2017-09-27', NULL),
(4, 2, 1, 3, 4, '2017-09-27', NULL),
(5, 2, 0, 4, 2, '2017-10-18', NULL),
(6, 1, 0, 3, 1, '2017-10-18', NULL),
(7, 4, 1, 2, 2, '2017-10-31', NULL),
(8, 3, 2, 1, 0, '2017-10-31', NULL),
(9, 2, 2, 1, 0, '2017-11-22', NULL),
(10, 4, 1, 3, 0, '2017-11-22', NULL),
(11, 1, 0, 4, 2, '2017-12-05', NULL),
(12, 3, 2, 2, 1, '2017-12-05', NULL),
(13, 5, 3, 6, 0, '2017-09-12', NULL),
(14, 7, 0, 8, 5, '2017-09-12', NULL),
(15, 8, 3, 5, 0, '2017-09-27', NULL),
(16, 6, 0, 7, 3, '2017-09-27', NULL),
(17, 6, 0, 8, 4, '2017-10-18', NULL),
(18, 5, 3, 7, 0, '2017-10-18', NULL),
(19, 8, 5, 6, 0, '2017-10-31', NULL),
(20, 7, 1, 5, 2, '2017-10-31', NULL),
(21, 6, 1, 5, 2, '2017-11-22', NULL),
(22, 8, 7, 7, 1, '2017-11-22', NULL),
(23, 5, 3, 8, 1, '2017-12-05', NULL),
(24, 7, 0, 6, 1, '2017-12-05', NULL),
(25, 9, 6, 10, 0, '2017-09-12', NULL),
(26, 11, 0, 12, 0, '2017-09-12', NULL),
(27, 10, 1, 11, 2, '2017-09-27', NULL),
(28, 12, 1, 9, 2, '2017-09-27', NULL),
(29, 10, 0, 12, 0, '2017-10-18', NULL),
(30, 9, 3, 11, 3, '2017-10-18', NULL),
(31, 12, 1, 10, 1, '2017-10-31', NULL),
(32, 11, 3, 9, 0, '2017-10-31', NULL),
(33, 10, 0, 9, 4, '2017-11-22', NULL),
(34, 12, 2, 11, 0, '2017-11-22', NULL),
(35, 9, 1, 12, 1, '2017-12-05', NULL),
(36, 11, 1, 10, 0, '2017-12-05', NULL),
(37, 13, 3, 14, 0, '2017-09-12', NULL),
(38, 15, 2, 16, 3, '2017-09-12', NULL),
(39, 16, 0, 13, 1, '2017-09-27', NULL),
(40, 14, 2, 15, 0, '2017-09-27', NULL),
(41, 14, 2, 16, 1, '2017-10-18', NULL),
(42, 13, 3, 15, 1, '2017-10-18', NULL),
(43, 16, 1, 14, 1, '2017-10-31', NULL),
(44, 15, 0, 13, 0, '2017-10-31', NULL),
(45, 14, 0, 13, 0, '2017-11-22', NULL),
(46, 16, 3, 15, 1, '2017-11-22', NULL),
(47, 13, 2, 16, 0, '2017-12-05', NULL),
(48, 15, 0, 14, 2, '2017-12-05', NULL),
(49, 17, 1, 18, 1, '2017-09-13', NULL),
(50, 19, 2, 20, 2, '2017-09-13', NULL),
(51, 20, 3, 17, 0, '2017-09-26', NULL),
(52, 18, 1, 19, 1, '2017-09-26', NULL),
(53, 18, 5, 20, 1, '2017-10-17', NULL),
(54, 17, 0, 19, 7, '2017-10-17', NULL),
(55, 20, 2, 18, 1, '2017-11-01', NULL),
(56, 19, 3, 17, 0, '2017-11-01', NULL),
(57, 18, 1, 17, 1, '2017-11-21', NULL),
(58, 20, 3, 19, 3, '2017-11-21', NULL),
(59, 17, 1, 20, 1, '2017-12-06', NULL),
(60, 19, 7, 18, 0, '2017-12-06', NULL),
(61, 21, 0, 22, 4, '2017-09-13', NULL),
(62, 23, 2, 24, 1, '2017-09-13', NULL),
(63, 24, 3, 21, 1, '2017-09-26', NULL),
(64, 22, 2, 23, 0, '2017-09-26', NULL),
(65, 22, 2, 24, 1, '2017-10-17', NULL),
(66, 21, 1, 23, 2, '2017-10-17', NULL),
(67, 24, 2, 22, 4, '2017-11-01', NULL),
(68, 23, 3, 21, 1, '2017-11-01', NULL),
(69, 22, 1, 21, 0, '2017-11-21', NULL),
(70, 24, 3, 23, 0, '2017-11-21', NULL),
(71, 21, 2, 24, 1, '2017-12-06', NULL),
(72, 23, 2, 22, 1, '2017-12-06', NULL),
(73, 25, 1, 26, 1, '2017-09-13', NULL),
(74, 27, 1, 28, 3, '2017-09-13', NULL),
(75, 28, 2, 25, 0, '2017-09-26', NULL),
(76, 26, 0, 27, 3, '2017-09-26', NULL),
(77, 26, 1, 28, 2, '2017-10-17', NULL),
(78, 25, 3, 27, 2, '2017-10-17', NULL),
(79, 28, 1, 26, 1, '2017-11-01', NULL),
(80, 27, 3, 25, 1, '2017-11-01', NULL),
(81, 28, 1, 27, 1, '2017-11-21', NULL),
(82, 26, 1, 25, 4, '2017-11-21', NULL),
(83, 25, 1, 28, 2, '2017-12-06', NULL),
(84, 27, 5, 26, 2, '2017-12-06', NULL),
(85, 29, 3, 30, 0, '2017-09-13', NULL),
(86, 31, 3, 32, 1, '2017-09-13', NULL),
(87, 32, 1, 29, 3, '2017-09-26', NULL),
(88, 30, 0, 31, 3, '2017-09-26', NULL),
(89, 30, 1, 32, 1, '2017-10-17', NULL),
(90, 29, 1, 31, 1, '2017-10-17', NULL),
(91, 32, 1, 30, 1, '2017-11-01', NULL),
(92, 31, 3, 29, 1, '2017-11-01', NULL),
(93, 30, 0, 29, 6, '2017-11-21', NULL),
(94, 32, 1, 31, 2, '2017-11-21', NULL),
(95, 29, 3, 32, 2, '2017-12-06', NULL),
(96, 31, 3, 30, 0, '2017-12-06', NULL);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `matchs17_UEFA`
--
ALTER TABLE `matchs17_UEFA`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `matchs17_UEFA`
--
ALTER TABLE `matchs17_UEFA`
  MODIFY `id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=97;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
