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
-- Table structure for table `equipes17_UEFA`
--

CREATE TABLE `equipes17_UEFA` (
  `id` int(10) UNSIGNED NOT NULL,
  `nom` varchar(100) DEFAULT NULL,
  `groupe` varchar(10) DEFAULT NULL,
  `points` int(10) DEFAULT NULL,
  `joues` int(10) DEFAULT NULL,
  `gagnes` int(10) DEFAULT NULL,
  `perdus` int(10) DEFAULT NULL,
  `nuls` int(10) DEFAULT NULL,
  `marques` int(10) DEFAULT NULL,
  `encaisses` int(10) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `equipes17_UEFA`
--

INSERT INTO `equipes17_UEFA` (`id`, `nom`, `groupe`, `points`, `joues`, `gagnes`, `perdus`, `nuls`, `marques`, `encaisses`) VALUES
(1, 'Benfica', 'A', 0, 6, 0, 6, 0, 1, 14),
(2, 'CSKA Moscow', 'A', 9, 6, 3, 3, 0, 8, 10),
(3, 'Manchester United', 'A', 15, 6, 5, 1, 0, 12, 3),
(4, 'Basel', 'A', 12, 6, 4, 2, 0, 11, 5),
(5, 'Bayern München', 'B', 15, 6, 5, 1, 0, 13, 6),
(6, 'Anderlecht', 'B', 3, 6, 1, 5, 0, 2, 17),
(7, 'Celtic', 'B', 3, 6, 1, 5, 0, 5, 18),
(8, 'Paris Saint-Germain', 'B', 15, 6, 5, 1, 0, 25, 4),
(9, 'Chelsea', 'C', 11, 6, 3, 1, 2, 16, 8),
(10, 'Qarabag', 'C', 2, 6, 0, 4, 2, 2, 14),
(11, 'Roma', 'C', 11, 6, 3, 1, 2, 9, 6),
(12, 'Atlético Madrid', 'C', 7, 6, 1, 1, 4, 5, 4),
(13, 'Barcelona', 'D', 14, 6, 4, 0, 2, 9, 1),
(14, 'Juventus', 'D', 11, 6, 3, 1, 2, 7, 5),
(15, 'Olympiacos', 'D', 1, 6, 0, 5, 1, 4, 13),
(16, 'Sporting CP', 'D', 7, 6, 2, 3, 1, 8, 9),
(17, 'Maribor', 'E', 3, 6, 0, 3, 3, 3, 16),
(18, 'Spartak Moscow', 'E', 6, 6, 1, 2, 3, 9, 13),
(19, 'Liverpool', 'E', 12, 6, 3, 0, 3, 23, 6),
(20, 'Sevilla', 'E', 9, 6, 2, 1, 3, 12, 12),
(21, 'Feyenoord', 'F', 3, 6, 1, 5, 0, 5, 14),
(22, 'Manchester City', 'F', 15, 6, 5, 1, 0, 14, 5),
(23, 'Shakhtar Donetsk', 'F', 12, 6, 4, 2, 0, 9, 9),
(24, 'Napoli', 'F', 6, 6, 2, 4, 0, 11, 11),
(25, 'RB Leipzig', 'G', 7, 6, 2, 3, 1, 10, 11),
(26, 'Monaco', 'G', 2, 6, 0, 4, 2, 6, 16),
(27, 'Porto', 'G', 10, 6, 3, 2, 1, 15, 10),
(28, 'Besiktas', 'G', 14, 6, 4, 0, 2, 11, 5),
(29, 'Real Madrid', 'H', 13, 6, 4, 1, 1, 17, 7),
(30, 'APOEL', 'H', 2, 6, 0, 4, 2, 2, 17),
(31, 'Tottenham Hotspur', 'H', 16, 6, 5, 0, 1, 15, 4),
(32, 'Borussia Dortmund', 'H', 2, 6, 0, 4, 2, 7, 13);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `equipes17_UEFA`
--
ALTER TABLE `equipes17_UEFA`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `equipes17_UEFA`
--
ALTER TABLE `equipes17_UEFA`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
