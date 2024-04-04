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
-- Table structure for table `matchs14_UEFA`
--

CREATE TABLE `matchs14_UEFA` (
  `id` int(11) UNSIGNED NOT NULL,
  `eq1` int(10) DEFAULT NULL,
  `score1` int(4) DEFAULT NULL,
  `eq2` int(10) DEFAULT NULL,
  `score2` int(4) DEFAULT NULL,
  `dateMatch` date DEFAULT NULL,
  `journee` int(3) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `matchs14_UEFA`
--

INSERT INTO `matchs14_UEFA` (`id`, `eq1`, `score1`, `eq2`, `score2`, `dateMatch`, `journee`) VALUES
(1, 1, 3, 2, 2, '2014-09-16', NULL),
(2, 3, 2, 4, 0, '2014-09-16', NULL),
(3, 5, 5, 6, 1, '2014-09-16', NULL),
(4, 7, 2, 8, 1, '2014-09-16', NULL),
(5, 9, 1, 10, 0, '2014-09-16', NULL),
(6, 11, 0, 12, 2, '2014-09-16', NULL),
(7, 13, 2, 14, 0, '2014-09-16', NULL),
(8, 15, 1, 16, 1, '2014-09-16', NULL),
(9, 17, 5, 18, 1, '2014-09-17', NULL),
(10, 19, 1, 20, 0, '2014-09-17', NULL),
(11, 21, 1, 22, 1, '2014-09-17', NULL),
(12, 23, 1, 24, 0, '2014-09-17', NULL),
(13, 25, 1, 26, 1, '2014-09-17', NULL),
(14, 27, 1, 28, 1, '2014-09-17', NULL),
(15, 29, 0, 30, 0, '2014-09-17', NULL),
(16, 31, 6, 32, 0, '2014-09-17', NULL),
(17, 2, 1, 3, 0, '2014-10-01', NULL),
(18, 4, 2, 1, 0, '2014-10-01', NULL),
(19, 6, 1, 7, 0, '2014-10-01', NULL),
(20, 8, 1, 5, 2, '2014-10-01', NULL),
(21, 12, 0, 9, 0, '2014-10-01', NULL),
(22, 10, 3, 11, 1, '2014-10-01', NULL),
(23, 14, 4, 15, 1, '2014-10-01', NULL),
(24, 16, 0, 13, 3, '2014-10-01', NULL),
(25, 18, 0, 19, 1, '2014-09-30', NULL),
(26, 20, 1, 17, 1, '2014-09-30', NULL),
(27, 24, 1, 21, 1, '2014-09-30', NULL),
(28, 22, 3, 23, 2, '2014-09-30', NULL),
(29, 28, 0, 25, 1, '2014-09-30', NULL),
(30, 26, 1, 27, 1, '2014-09-30', NULL),
(31, 32, 2, 29, 1, '2014-09-30', NULL),
(32, 30, 2, 31, 2, '2014-09-30', NULL),
(33, 2, 5, 4, 0, '2014-10-22', NULL),
(34, 1, 1, 3, 0, '2014-10-22', NULL),
(35, 8, 1, 6, 0, '2014-10-22', NULL),
(36, 7, 0, 5, 3, '2014-10-22', NULL),
(37, 9, 0, 11, 0, '2014-10-22', NULL),
(38, 10, 2, 12, 0, '2014-10-22', NULL),
(39, 16, 1, 14, 2, '2014-10-22', NULL),
(40, 15, 0, 13, 4, '2014-10-22', NULL),
(41, 18, 2, 20, 2, '2014-10-21', NULL),
(42, 17, 1, 19, 7, '2014-10-21', NULL),
(43, 23, 3, 21, 1, '2014-10-21', NULL),
(44, 24, 0, 22, 1, '2014-10-21', NULL),
(45, 25, 6, 27, 0, '2014-10-21', NULL),
(46, 26, 4, 28, 3, '2014-10-21', NULL),
(47, 31, 2, 29, 1, '2014-10-21', NULL),
(48, 32, 0, 30, 7, '2014-10-21', NULL),
(49, 4, 0, 2, 2, '2014-11-04', NULL),
(50, 3, 3, 1, 2, '2014-11-04', NULL),
(51, 6, 4, 8, 0, '2014-11-04', NULL),
(52, 5, 1, 7, 0, '2014-11-04', NULL),
(53, 12, 1, 10, 2, '2014-11-04', NULL),
(54, 11, 1, 9, 0, '2014-11-04', NULL),
(55, 14, 3, 16, 3, '2014-11-04', NULL),
(56, 13, 4, 15, 1, '2014-11-04', NULL),
(57, 19, 2, 17, 0, '2014-11-05', NULL),
(58, 20, 1, 18, 2, '2014-11-05', NULL),
(59, 21, 0, 23, 2, '2014-11-05', NULL),
(60, 22, 1, 24, 0, '2014-11-05', NULL),
(61, 27, 1, 25, 1, '2014-11-05', NULL),
(62, 28, 4, 26, 2, '2014-11-05', NULL),
(63, 29, 0, 31, 2, '2014-11-05', NULL),
(64, 30, 5, 32, 0, '2014-11-05', NULL),
(65, 2, 4, 1, 0, '2014-11-26', NULL),
(66, 4, 0, 3, 2, '2014-11-26', NULL),
(67, 6, 0, 5, 1, '2014-11-26', NULL),
(68, 8, 2, 7, 2, '2014-11-26', NULL),
(69, 12, 1, 11, 0, '2014-11-26', NULL),
(70, 10, 0, 9, 1, '2014-11-26', NULL),
(71, 14, 2, 13, 0, '2014-11-26', NULL),
(72, 16, 2, 15, 0, '2014-11-26', NULL),
(73, 18, 1, 17, 1, '2014-11-25', NULL),
(74, 20, 3, 19, 2, '2014-11-25', NULL),
(75, 22, 3, 21, 1, '2014-11-25', NULL),
(76, 24, 0, 23, 4, '2014-11-25', NULL),
(77, 26, 0, 25, 5, '2014-11-25', NULL),
(78, 28, 3, 27, 1, '2014-11-25', NULL),
(79, 32, 0, 31, 3, '2014-11-25', NULL),
(80, 30, 0, 29, 1, '2014-11-25', NULL),
(81, 3, 0, 2, 0, '2014-12-09', NULL),
(82, 1, 4, 4, 2, '2014-12-09', NULL),
(83, 7, 1, 6, 1, '2014-12-09', NULL),
(84, 5, 4, 8, 0, '2014-12-09', NULL),
(85, 9, 2, 12, 0, '2014-12-09', NULL),
(86, 11, 0, 10, 0, '2014-12-09', NULL),
(87, 15, 1, 14, 4, '2014-12-09', NULL),
(88, 13, 1, 16, 1, '2014-12-09', NULL),
(89, 17, 0, 20, 2, '2014-12-10', NULL),
(90, 19, 3, 18, 0, '2014-12-10', NULL),
(91, 21, 4, 24, 0, '2014-12-10', NULL),
(92, 23, 3, 22, 1, '2014-12-10', NULL),
(93, 25, 3, 28, 1, '2014-12-10', NULL),
(94, 27, 0, 26, 1, '2014-12-10', NULL),
(95, 29, 2, 32, 0, '2014-12-10', NULL),
(96, 31, 1, 30, 1, '2014-12-10', NULL);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `matchs14_UEFA`
--
ALTER TABLE `matchs14_UEFA`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `matchs14_UEFA`
--
ALTER TABLE `matchs14_UEFA`
  MODIFY `id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=97;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
