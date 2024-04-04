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
-- Table structure for table `equipes14_UEFA`
--

CREATE TABLE `equipes14_UEFA` (
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
-- Dumping data for table `equipes14_UEFA`
--

INSERT INTO `equipes14_UEFA` (`id`, `nom`, `groupe`, `points`, `joues`, `gagnes`, `perdus`, `nuls`, `marques`, `encaisses`) VALUES
(1, 'Olympiacos Piraeus FC', 'Group A', 9, 6, 3, 3, 0, 10, 13),
(2, 'Atlético Madrid', 'Group A', 13, 6, 4, 1, 1, 14, 3),
(3, 'Juventus', 'Group A', 10, 6, 3, 2, 1, 7, 4),
(4, 'Malmö FF', 'Group A', 3, 6, 1, 5, 0, 4, 15),
(5, 'Real Madrid', 'Group B', 18, 6, 6, 0, 0, 16, 2),
(6, 'FC Basel', 'Group B', 7, 6, 2, 3, 1, 7, 8),
(7, 'Liverpool FC', 'Group B', 5, 6, 1, 3, 2, 5, 9),
(8, 'PFC Ludogorets Razgrad', 'Group B', 4, 6, 1, 4, 1, 5, 14),
(9, 'AS Monaco', 'Group C', 11, 6, 3, 1, 2, 4, 1),
(10, 'Bayer 04 Leverkusen', 'Group C', 10, 6, 3, 2, 1, 7, 4),
(11, 'SL Benfica', 'Group C', 5, 6, 1, 3, 2, 2, 6),
(12, 'Zenit St. Petersburg', 'Group C', 7, 6, 2, 3, 1, 4, 6),
(13, 'Borussia Dortmund', 'Group D', 13, 6, 4, 1, 1, 14, 4),
(14, 'Arsenal FC', 'Group D', 13, 6, 4, 1, 1, 15, 8),
(15, 'Galatasaray Istanbul', 'Group D', 1, 6, 0, 5, 1, 4, 19),
(16, 'RSC Anderlecht', 'Group D', 6, 6, 1, 2, 3, 8, 10),
(17, 'AS Roma', 'Group E', 5, 6, 1, 3, 2, 8, 14),
(18, 'PFC CSKA Moskva', 'Group E', 5, 6, 1, 3, 2, 6, 13),
(19, 'Bayern München', 'Group E', 15, 6, 5, 1, 0, 16, 4),
(20, 'Manchester City FC', 'Group E', 8, 6, 2, 2, 2, 9, 8),
(21, 'Ajax Amsterdam', 'Group F', 5, 6, 1, 3, 2, 8, 10),
(22, 'Paris Saint-Germain', 'Group F', 13, 6, 4, 1, 1, 10, 7),
(23, 'FC Barcelona', 'Group F', 15, 6, 5, 1, 0, 15, 5),
(24, 'APOEL Nicosia FC', 'Group F', 1, 6, 0, 5, 1, 1, 12),
(25, 'Chelsea FC', 'Group G', 14, 6, 4, 0, 2, 17, 3),
(26, 'FC Schalke 04', 'Group G', 8, 6, 2, 2, 2, 9, 14),
(27, 'NK Maribor', 'Group G', 3, 6, 0, 3, 3, 4, 13),
(28, 'Sporting CP', 'Group G', 7, 6, 2, 3, 1, 12, 12),
(29, 'Athletic Club Bilbao', 'Group H', 7, 6, 2, 3, 1, 5, 6),
(30, 'FC Shakhtar Donetsk', 'Group H', 9, 6, 2, 1, 3, 15, 4),
(31, 'FC Porto', 'Group H', 14, 6, 4, 0, 2, 16, 4),
(32, 'FC BATE Borisov', 'Group H', 3, 6, 1, 5, 0, 2, 24);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `equipes14_UEFA`
--
ALTER TABLE `equipes14_UEFA`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `equipes14_UEFA`
--
ALTER TABLE `equipes14_UEFA`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
