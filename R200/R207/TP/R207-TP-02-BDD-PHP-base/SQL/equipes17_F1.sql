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
-- Table structure for table `equipes17_F1`
--

CREATE TABLE `equipes17_F1` (
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
-- Dumping data for table `equipes17_F1`
--

INSERT INTO `equipes17_F1` (`id`, `nom`, `groupe`, `points`, `joues`, `gagnes`, `perdus`, `nuls`, `marques`, `encaisses`) VALUES
(1, 'Monaco', 'D1', 80, 38, 24, 6, 8, 85, 45),
(2, 'Toulouse', 'D1', 37, 38, 9, 19, 10, 38, 54),
(3, 'Lyon', 'D1', 78, 38, 23, 6, 9, 87, 43),
(4, 'Strasbourg', 'D1', 38, 38, 9, 18, 11, 44, 67),
(5, 'Metz', 'D1', 26, 38, 6, 24, 8, 34, 76),
(6, 'Guingamp', 'D1', 47, 38, 12, 15, 11, 48, 59),
(7, 'Montpellier', 'D1', 51, 38, 11, 9, 18, 36, 33),
(8, 'Caen', 'D1', 38, 38, 10, 20, 8, 27, 52),
(9, 'Paris SG', 'D1', 93, 38, 29, 3, 6, 108, 29),
(10, 'Amiens', 'D1', 45, 38, 12, 17, 9, 37, 42),
(11, 'St Etienne', 'D1', 55, 38, 15, 13, 10, 47, 50),
(12, 'Nice', 'D1', 54, 38, 15, 14, 9, 53, 52),
(13, 'Troyes', 'D1', 33, 38, 9, 23, 6, 32, 59),
(14, 'Rennes', 'D1', 58, 38, 16, 12, 10, 50, 44),
(15, 'Angers', 'D1', 41, 38, 9, 15, 14, 42, 52),
(16, 'Bordeaux', 'D1', 55, 38, 16, 15, 7, 53, 48),
(17, 'Lille', 'D1', 38, 38, 10, 20, 8, 41, 67),
(18, 'Nantes', 'D1', 52, 38, 14, 14, 10, 36, 41),
(19, 'Marseille', 'D1', 77, 38, 22, 5, 11, 80, 47),
(20, 'Dijon', 'D1', 48, 38, 13, 16, 9, 55, 73);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `equipes17_F1`
--
ALTER TABLE `equipes17_F1`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `equipes17_F1`
--
ALTER TABLE `equipes17_F1`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
