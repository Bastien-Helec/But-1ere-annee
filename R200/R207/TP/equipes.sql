-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Hôte : localhost
-- Généré le : mar. 07 fév. 2023 à 09:35
-- Version du serveur : 10.5.18-MariaDB-log
-- Version de PHP : 7.4.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `db_HELEC`
--

-- --------------------------------------------------------

--
-- Structure de la table `equipes`
--

CREATE TABLE `equipes` (
  `id` int(255) NOT NULL,
  `nom` varchar(255) NOT NULL,
  `groupe` varchar(255) NOT NULL,
  `point` int(255) NOT NULL,
  `joues` int(255) NOT NULL,
  `gagnes` int(255) NOT NULL,
  `perdus` int(255) NOT NULL,
  `nuls` int(255) NOT NULL,
  `marques` int(255) NOT NULL,
  `encaisses` int(255) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Déchargement des données de la table `equipes`
--

INSERT INTO `equipes` (`id`, `nom`, `groupe`, `point`, `joues`, `gagnes`, `perdus`, `nuls`, `marques`, `encaisses`) VALUES
(1, 'Marseille', '', 0, 0, 0, 0, 0, 0, 0),
(2, 'Toulouse', '', 0, 0, 0, 0, 0, 0, 0),
(3, 'Angers', '', 0, 0, 0, 0, 0, 0, 0),
(4, 'Nimes', '', 0, 0, 0, 0, 0, 0, 0),
(5, 'Lille', '', 0, 0, 0, 0, 0, 0, 0),
(6, 'Rennes', '', 0, 0, 0, 0, 0, 0, 0),
(7, 'Montpellier', '', 0, 0, 0, 0, 0, 0, 0),
(8, 'Dijon', '', 0, 0, 0, 0, 0, 0, 0),
(9, 'Nantes', '', 0, 0, 0, 0, 0, 0, 0),
(10, 'Monaco', '', 0, 0, 0, 0, 0, 0, 0),
(11, 'Nice', '', 0, 0, 0, 0, 0, 0, 0),
(12, 'Reims', '', 0, 0, 0, 0, 0, 0, 0),
(13, 'St Etienne', '', 0, 0, 0, 0, 0, 0, 0),
(14, 'Guingamp', '', 0, 0, 0, 0, 0, 0, 0),
(15, 'Bordeaux', '', 0, 0, 0, 0, 0, 0, 0),
(16, 'Strasbourg', '', 0, 0, 0, 0, 0, 0, 0),
(17, 'Lyon', '', 0, 0, 0, 0, 0, 0, 0),
(18, 'Amiens', '', 0, 0, 0, 0, 0, 0, 0),
(19, 'Paris SG', '', 0, 0, 0, 0, 0, 0, 0),
(20, 'Caen', '', 0, 0, 0, 0, 0, 0, 0),
(22, 'Béziers', ' ', 0, 0, 0, 0, 0, 0, 0);

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `equipes`
--
ALTER TABLE `equipes`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `equipes`
--
ALTER TABLE `equipes`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
