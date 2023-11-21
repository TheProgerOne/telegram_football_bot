-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Хост: 127.0.0.1:3306
-- Время создания: Ноя 19 2023 г., 17:50
-- Версия сервера: 5.6.51-log
-- Версия PHP: 7.2.34

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `test`
--

-- --------------------------------------------------------

--
-- Структура таблицы `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `name` varchar(250) COLLATE utf8mb4_unicode_ci NOT NULL,
  `tell_number` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Дамп данных таблицы `users`
--

INSERT INTO `users` (`id`, `user_id`, `name`, `tell_number`) VALUES
(1, 752736386, 'FDHUNT', ''),
(2, 777, 'jamshid', ''),
(3, 752736386, 'FDHUNT', ''),
(4, 777, 'jamshid', ''),
(5, 752736386, 'FDHUNT', ''),
(6, 777, 'jamshid', ''),
(7, 752736386, 'FDHUNT', ''),
(8, 777, 'jamshid', ''),
(9, 752736386, 'FDHUNT', ''),
(10, 777, 'jamshid', ''),
(11, 752736386, 'FDHUNT', ''),
(12, 777, 'jamshid', ''),
(13, 777, 'jamshid', ''),
(14, 777, 'jamshid', ''),
(15, 752736386, 'FDHUNT', ''),
(16, 777, 'jamshid', ''),
(17, 752736386, 'FDHUNT', ''),
(18, 777, 'jamshid', ''),
(19, 777, 'jamshid', ''),
(20, 777, 'jamshid', ''),
(21, 777, 'jamshid', ''),
(22, 777, 'jamshid', ''),
(23, 777, 'jamshid', ''),
(24, 777, 'jamshid', ''),
(25, 777, 'jamshid', ''),
(26, 777, 'jamshid', ''),
(27, 777, 'jamshid', ''),
(28, 777, 'jamshid', ''),
(29, 777, 'jamshid', ''),
(30, 777, 'jamshid', ''),
(31, 777, 'jamshid', ''),
(32, 777, 'jamshid', ''),
(33, 777, 'jamshid', ''),
(34, 777, 'jamshid', ''),
(35, 777, 'jamshid', ''),
(36, 777, 'jamshid', ''),
(37, 777, 'jamshid', ''),
(38, 777, 'jamshid', ''),
(39, 777, 'jamshid', ''),
(40, 777, 'jamshid', ''),
(41, 777, 'jamshid', ''),
(42, 777, 'jamshid', ''),
(43, 777, 'jamshid', ''),
(44, 777, 'jamshid', ''),
(45, 777, 'jamshid', ''),
(46, 777, 'jamshid', ''),
(47, 777, 'jamshid', ''),
(48, 777, 'jamshid', ''),
(49, 777, 'jamshid', ''),
(50, 777, 'jamshid', ''),
(51, 777, 'jamshid', ''),
(52, 777, 'jamshid', ''),
(53, 777, 'jamshid', ''),
(54, 777, 'jamshid', ''),
(55, 777, 'jamshid', ''),
(56, 777, 'jamshid', ''),
(57, 777, 'jamshid', ''),
(58, 777, 'jamshid', ''),
(59, 777, 'jamshid', ''),
(60, 777, 'jamshid', ''),
(61, 777, 'jamshid', ''),
(62, 777, 'jamshid', ''),
(63, 777, 'jamshid', ''),
(64, 777, 'jamshid', ''),
(65, 777, 'jamshid', ''),
(66, 777, 'jamshid', ''),
(67, 777, 'jamshid', ''),
(68, 777, 'jamshid', ''),
(69, 777, 'jamshid', ''),
(70, 777, 'jamshid', ''),
(71, 777, 'jamshid', ''),
(72, 777, 'jamshid', ''),
(73, 777, 'jamshid', ''),
(74, 777, 'jamshid', ''),
(75, 777, 'jamshid', ''),
(76, 777, 'jamshid', ''),
(77, 777, 'jamshid', ''),
(78, 777, 'jamshid', ''),
(79, 777, 'jamshid', ''),
(80, 777, 'jamshid', ''),
(81, 777, 'jamshid', ''),
(82, 777, 'jamshid', ''),
(83, 777, 'jamshid', ''),
(84, 752736386, 'FDHUNT', ''),
(85, 1089509098, 'prog', ''),
(86, 752736386, 'FDHUNT', ''),
(87, 777, 'jamshid', ''),
(88, 752736386, 'FDHUNT', ''),
(89, 777, 'jamshid', ''),
(90, 752736386, 'FDHUNT', ''),
(91, 777, 'jamshid', ''),
(92, 752736386, 'FDHUNT', ''),
(93, 777, 'jamshid', ''),
(94, 777, 'jamshid', ''),
(95, 777, 'jamshid', ''),
(96, 752736386, 'FDHUNT', ''),
(97, 777, 'jamshid', ''),
(98, 752736386, 'FDHUNT', ''),
(99, 777, 'jamshid', ''),
(100, 777, 'jamshid', ''),
(101, 777, 'jamshid', ''),
(102, 777, 'jamshid', ''),
(103, 777, 'jamshid', ''),
(104, 777, 'jamshid', ''),
(105, 752736386, 'FDHUNT', ''),
(106, 777, 'jamshid', ''),
(107, 752736386, 'FDHUNT', ''),
(108, 777, 'jamshid', ''),
(109, 752736386, 'FDHUNT', ''),
(110, 777, 'jamshid', ''),
(111, 752736386, 'FDHUNT', ''),
(112, 777, 'jamshid', ''),
(113, 752736386, 'FDHUNT', ''),
(114, 777, 'jamshid', ''),
(115, 752736386, 'FDHUNT', ''),
(116, 777, 'jamshid', ''),
(117, 752736386, 'FDHUNT', ''),
(118, 683186972, '.', ''),
(119, 1688660441, 'Ismailbek .', ''),
(120, 752736386, 'FDHUNT', ''),
(121, 1688660441, 'Ismailbek .', ''),
(122, 752736386, 'FDHUNT', ''),
(123, 752736386, 'FDHUNT', ''),
(124, 2147483647, 'Айдар', ''),
(125, 1089509098, 'prog', '');

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=126;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
