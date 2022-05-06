-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 30-12-2021 a las 03:03:32
-- Versión del servidor: 10.4.20-MariaDB
-- Versión de PHP: 8.0.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `axypruebas2`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `actividadescristianas`
--

CREATE TABLE `actividadescristianas` (
  `activcris_id` int(11) NOT NULL,
  `activcris_nombre` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `actividadescristianas`
--

INSERT INTO `actividadescristianas` (`activcris_id`, `activcris_nombre`) VALUES
(1, 'Escuela dominical'),
(2, 'Grupo de danzas'),
(3, 'Grupo de oración'),
(4, 'Escuela dominical'),
(5, 'Grupo de danzas'),
(6, 'Grupo de oración');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add categoria', 7, 'add_categoria'),
(26, 'Can change categoria', 7, 'change_categoria'),
(27, 'Can delete categoria', 7, 'delete_categoria'),
(28, 'Can view categoria', 7, 'view_categoria'),
(29, 'Can add post', 8, 'add_post'),
(30, 'Can change post', 8, 'change_post'),
(31, 'Can delete post', 8, 'delete_post'),
(32, 'Can view post', 8, 'view_post'),
(33, 'Can add Religion', 9, 'add_religion'),
(34, 'Can change Religion', 9, 'change_religion'),
(35, 'Can delete Religion', 9, 'delete_religion'),
(36, 'Can view Religion', 9, 'view_religion'),
(37, 'Can add Sexo', 10, 'add_sexo'),
(38, 'Can change Sexo', 10, 'change_sexo'),
(39, 'Can delete Sexo', 10, 'delete_sexo'),
(40, 'Can view Sexo', 10, 'view_sexo'),
(41, 'Can add Rendimiento Academico', 11, 'add_rendimientoacademico'),
(42, 'Can change Rendimiento Academico', 11, 'change_rendimientoacademico'),
(43, 'Can delete Rendimiento Academico', 11, 'delete_rendimientoacademico'),
(44, 'Can view Rendimiento Academico', 11, 'view_rendimientoacademico'),
(45, 'Can add Educación Formal', 12, 'add_educacionformal'),
(46, 'Can change Educación Formal', 12, 'change_educacionformal'),
(47, 'Can delete Educación Formal', 12, 'delete_educacionformal'),
(48, 'Can view Educación Formal', 12, 'view_educacionformal'),
(49, 'Can add GrupoEtareo', 13, 'add_grupoetareo'),
(50, 'Can change GrupoEtareo', 13, 'change_grupoetareo'),
(51, 'Can delete GrupoEtareo', 13, 'delete_grupoetareo'),
(52, 'Can view GrupoEtareo', 13, 'view_grupoetareo'),
(53, 'Can add Actividades Cristianas', 14, 'add_actividadescristianas'),
(54, 'Can change Actividades Cristianas', 14, 'change_actividadescristianas'),
(55, 'Can delete Actividades Cristianas', 14, 'delete_actividadescristianas'),
(56, 'Can view Actividades Cristianas', 14, 'view_actividadescristianas'),
(57, 'Can add Ciudad', 15, 'add_ciudades'),
(58, 'Can change Ciudad', 15, 'change_ciudades'),
(59, 'Can delete Ciudad', 15, 'delete_ciudades'),
(60, 'Can view Ciudad', 15, 'view_ciudades'),
(61, 'Can add Departamento', 16, 'add_departamento'),
(62, 'Can change Departamento', 16, 'change_departamento'),
(63, 'Can delete Departamento', 16, 'delete_departamento'),
(64, 'Can view Departamento', 16, 'view_departamento'),
(65, 'Can add Beneficiario', 17, 'add_beneficiario'),
(66, 'Can change Beneficiario', 17, 'change_beneficiario'),
(67, 'Can delete Beneficiario', 17, 'delete_beneficiario'),
(68, 'Can view Beneficiario', 17, 'view_beneficiario'),
(69, 'Can add Hobbie', 18, 'add_hobbies'),
(70, 'Can change Hobbie', 18, 'change_hobbies'),
(71, 'Can delete Hobbie', 18, 'delete_hobbies'),
(72, 'Can view Hobbie', 18, 'view_hobbies'),
(73, 'Can add Materia', 19, 'add_materias'),
(74, 'Can change Materia', 19, 'change_materias'),
(75, 'Can delete Materia', 19, 'delete_materias'),
(76, 'Can view Materia', 19, 'view_materias'),
(77, 'Can add Deber', 20, 'add_deberes'),
(78, 'Can change Deber', 20, 'change_deberes'),
(79, 'Can delete Deber', 20, 'delete_deberes'),
(80, 'Can view Deber', 20, 'view_deberes'),
(81, 'Can add Historia Clínica', 21, 'add_historiaclinica'),
(82, 'Can change Historia Clínica', 21, 'change_historiaclinica'),
(83, 'Can delete Historia Clínica', 21, 'delete_historiaclinica'),
(84, 'Can view Historia Clínica', 21, 'view_historiaclinica'),
(85, 'Can add Discapacidad física', 22, 'add_discapacidadesfisicas'),
(86, 'Can change Discapacidad física', 22, 'change_discapacidadesfisicas'),
(87, 'Can delete Discapacidad física', 22, 'delete_discapacidadesfisicas'),
(88, 'Can view Discapacidad física', 22, 'view_discapacidadesfisicas'),
(89, 'Can add Discapacidad mental', 23, 'add_discapacidadesmentales'),
(90, 'Can change Discapacidad mental', 23, 'change_discapacidadesmentales'),
(91, 'Can delete Discapacidad mental', 23, 'delete_discapacidadesmentales'),
(92, 'Can view Discapacidad mental', 23, 'view_discapacidadesmentales'),
(93, 'Can add Enfermedad crónica', 24, 'add_enfermedadcronica'),
(94, 'Can change Enfermedad crónica', 24, 'change_enfermedadcronica'),
(95, 'Can delete Enfermedad crónica', 24, 'delete_enfermedadcronica'),
(96, 'Can view Enfermedad crónica', 24, 'view_enfermedadcronica');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$260000$9rnF1RLNisMj3JQFcScuZx$XnL5XRpcjiLWqK/8HrMCJ+fhG7gh0CRneDfcY+GXZsA=', '2021-10-26 01:47:14.742611', 1, 'admin', '', '', 'natymendieta29@gmail.com', 1, 1, '2021-10-12 01:54:51.150181');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `beneficiario`
--

CREATE TABLE `beneficiario` (
  `benef_id` varchar(20) NOT NULL,
  `benef_nombres` varchar(200) NOT NULL,
  `benef_apellidos` varchar(200) NOT NULL,
  `benef_nombrepref` varchar(200) NOT NULL,
  `benef_fechanac` date NOT NULL,
  `benef_edad` int(10) UNSIGNED NOT NULL CHECK (`benef_edad` >= 0),
  `benef_huerfano` tinyint(1) NOT NULL,
  `benef_nav` tinyint(1) NOT NULL,
  `benef_barrio` varchar(200) DEFAULT NULL,
  `benef_direccion` varchar(200) NOT NULL,
  `benef_telefono` bigint(20) DEFAULT NULL,
  `benef_correo` varchar(120) NOT NULL,
  `benef_img` varchar(100) NOT NULL,
  `benef_created` datetime(6) NOT NULL,
  `benef_updated` datetime(6) NOT NULL,
  `benef_activcrist` int(11) NOT NULL,
  `benef_ciudad` int(11) NOT NULL,
  `benef_departamento` int(11) NOT NULL,
  `benef_eduformal` int(11) NOT NULL,
  `benef_grupoeta` int(11) NOT NULL,
  `benef_religion` int(11) NOT NULL,
  `benef_rendiaca` int(11) NOT NULL,
  `benef_sexo` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `beneficiario`
--

INSERT INTO `beneficiario` (`benef_id`, `benef_nombres`, `benef_apellidos`, `benef_nombrepref`, `benef_fechanac`, `benef_edad`, `benef_huerfano`, `benef_nav`, `benef_barrio`, `benef_direccion`, `benef_telefono`, `benef_correo`, `benef_img`, `benef_created`, `benef_updated`, `benef_activcrist`, `benef_ciudad`, `benef_departamento`, `benef_eduformal`, `benef_grupoeta`, `benef_religion`, `benef_rendiaca`, `benef_sexo`) VALUES
('30506040', 'CAROLINE', 'CARRILLO LOPEZ', 'CARO', '2015-08-13', 10, 1, 0, 'LOS CUSULES', 'CALLE 30 20 15', 3185263020, 'CARO@GMAIL.COM', 'null', '2021-10-12 02:09:48.771384', '2021-10-12 02:09:48.771384', 1, 1, 1, 1, 1, 1, 1, 2),
('50203060', 'CARLOS', 'MARIN ESPINOSA', 'CARLLITOS', '2014-11-15', 12, 1, 0, 'LAS BRISAS', 'CALLE 20 15 50', 3205090, 'CARLOS@GMAIL.COM', 'null', '2021-10-13 00:34:25.577186', '2021-10-13 00:34:25.577186', 1, 1, 1, 2, 2, 1, 3, 1),
('6030908010', 'LUCAS', 'MARTINEZ', 'LUKIS', '2013-10-07', 8, 1, 0, 'LAS FLORES', 'CALLE 20 #20-50', 3186502030, 'LUKIS@GMAIL.COM', 'null', '2021-10-13 00:41:43.318951', '2021-10-13 00:41:43.318951', 2, 1, 1, 1, 1, 2, 1, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `beneficiario_benef_deberes`
--

CREATE TABLE `beneficiario_benef_deberes` (
  `id` int(11) NOT NULL,
  `beneficiario_id` varchar(20) NOT NULL,
  `deberes_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `beneficiario_benef_deberes`
--

INSERT INTO `beneficiario_benef_deberes` (`id`, `beneficiario_id`, `deberes_id`) VALUES
(1, '30506040', 1),
(2, '50203060', 2),
(3, '6030908010', 3);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `beneficiario_benef_hobbies`
--

CREATE TABLE `beneficiario_benef_hobbies` (
  `id` int(11) NOT NULL,
  `beneficiario_id` varchar(20) NOT NULL,
  `hobbies_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `beneficiario_benef_hobbies`
--

INSERT INTO `beneficiario_benef_hobbies` (`id`, `beneficiario_id`, `hobbies_id`) VALUES
(1, '30506040', 1),
(2, '50203060', 1),
(3, '6030908010', 3);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `beneficiario_benef_materias`
--

CREATE TABLE `beneficiario_benef_materias` (
  `id` int(11) NOT NULL,
  `beneficiario_id` varchar(20) NOT NULL,
  `materias_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `beneficiario_benef_materias`
--

INSERT INTO `beneficiario_benef_materias` (`id`, `beneficiario_id`, `materias_id`) VALUES
(1, '30506040', 1),
(2, '50203060', 2),
(3, '6030908010', 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `blog_categoria`
--

CREATE TABLE `blog_categoria` (
  `id` bigint(20) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `blog_categoria`
--

INSERT INTO `blog_categoria` (`id`, `nombre`, `created`, `updated`) VALUES
(1, 'DEPORTIVO', '2021-10-14 00:06:38.049961', '2021-10-14 00:06:38.049961'),
(2, 'Fisica', '2021-10-14 00:07:12.480952', '2021-10-14 00:07:12.480952'),
(3, 'Cognitiva', '2021-10-14 00:07:18.481064', '2021-10-14 00:07:18.481064'),
(4, 'Emocional', '2021-10-14 00:07:27.725160', '2021-10-14 00:07:27.725160'),
(5, 'Social', '2021-10-14 00:07:32.857101', '2021-10-14 00:07:32.857101');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `blog_post`
--

CREATE TABLE `blog_post` (
  `id` bigint(20) NOT NULL,
  `titulo` varchar(50) NOT NULL,
  `contenido` varchar(1000) NOT NULL,
  `imagen` varchar(100) DEFAULT NULL,
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) NOT NULL,
  `autor_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `blog_post`
--

INSERT INTO `blog_post` (`id`, `titulo`, `contenido`, `imagen`, `created`, `updated`, `autor_id`) VALUES
(1, 'Nuevo Post de muestra', 'lorem ipsum lorem ipsum lorem ipsum', 'blog/imagen1_p0kpi28.jpg', '2021-10-14 00:08:21.336818', '2021-10-14 00:08:21.336818', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `blog_post_categorias`
--

CREATE TABLE `blog_post_categorias` (
  `id` int(11) NOT NULL,
  `post_id` bigint(20) NOT NULL,
  `categoria_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `blog_post_categorias`
--

INSERT INTO `blog_post_categorias` (`id`, `post_id`, `categoria_id`) VALUES
(1, 1, 4);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ciudades`
--

CREATE TABLE `ciudades` (
  `ciu_id` int(11) NOT NULL,
  `ciu_nombre` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `ciudades`
--

INSERT INTO `ciudades` (`ciu_id`, `ciu_nombre`) VALUES
(1, 'Montelíbano'),
(2, 'Monteria'),
(3, 'Cerete');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `deberes`
--

CREATE TABLE `deberes` (
  `deb_id` int(11) NOT NULL,
  `deb_nombre` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `deberes`
--

INSERT INTO `deberes` (`deb_id`, `deb_nombre`) VALUES
(1, 'Lavado de ropa'),
(2, 'Acarrear agua'),
(3, 'Recoger Leña'),
(4, 'Cuidado niños'),
(5, 'Jardineria/agricultura'),
(6, 'Tender camas');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `departamento`
--

CREATE TABLE `departamento` (
  `dep_id` int(11) NOT NULL,
  `dep_nombre` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `departamento`
--

INSERT INTO `departamento` (`dep_id`, `dep_nombre`) VALUES
(1, 'Cordoba'),
(2, 'Cesar'),
(3, 'Bolivar'),
(4, 'Atlántico'),
(5, 'Antioquia'),
(6, 'Guajira');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `discapacidadesfisicas`
--

CREATE TABLE `discapacidadesfisicas` (
  `id` bigint(20) NOT NULL,
  `disfisica_nombre` varchar(100) NOT NULL,
  `disfisica_descripcion` longtext DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `discapacidadesfisicas`
--

INSERT INTO `discapacidadesfisicas` (`id`, `disfisica_nombre`, `disfisica_descripcion`) VALUES
(1, 'Ciego', ''),
(2, 'Sordo', ''),
(3, 'Invalido de piernas', '');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `discapacidadesmentales`
--

CREATE TABLE `discapacidadesmentales` (
  `id` bigint(20) NOT NULL,
  `dismental_nombre` varchar(100) NOT NULL,
  `dismental_descripcion` longtext DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `discapacidadesmentales`
--

INSERT INTO `discapacidadesmentales` (`id`, `dismental_nombre`, `dismental_descripcion`) VALUES
(1, 'Retraso mental', ''),
(2, 'Sindrome de Down', ''),
(3, 'Esquizofrenia', '');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2021-10-12 01:55:35.866526', '1', 'Montelíbano', 1, '[{\"added\": {}}]', 15, 1),
(2, '2021-10-12 01:55:39.960378', '2', 'Monteria', 1, '[{\"added\": {}}]', 15, 1),
(3, '2021-10-12 01:55:42.925499', '3', 'Cerete', 1, '[{\"added\": {}}]', 15, 1),
(4, '2021-10-12 01:55:51.492568', '1', 'Lavado de ropa', 1, '[{\"added\": {}}]', 20, 1),
(5, '2021-10-12 01:55:54.259825', '2', 'Acarrear agua', 1, '[{\"added\": {}}]', 20, 1),
(6, '2021-10-12 01:55:56.989355', '3', 'Recoger Leña', 1, '[{\"added\": {}}]', 20, 1),
(7, '2021-10-12 01:56:00.031670', '4', 'Cuidado niños', 1, '[{\"added\": {}}]', 20, 1),
(8, '2021-10-12 01:56:02.495673', '5', 'Jardineria/agricultura', 1, '[{\"added\": {}}]', 20, 1),
(9, '2021-10-12 01:56:05.153479', '6', 'Tender camas', 1, '[{\"added\": {}}]', 20, 1),
(10, '2021-10-12 01:56:12.774250', '1', 'Cordoba', 1, '[{\"added\": {}}]', 16, 1),
(11, '2021-10-12 01:56:15.547516', '2', 'Cesar', 1, '[{\"added\": {}}]', 16, 1),
(12, '2021-10-12 01:56:18.218635', '3', 'Bolivar', 1, '[{\"added\": {}}]', 16, 1),
(13, '2021-10-12 01:56:21.338460', '4', 'Atlántico', 1, '[{\"added\": {}}]', 16, 1),
(14, '2021-10-12 01:56:23.837733', '5', 'Antioquia', 1, '[{\"added\": {}}]', 16, 1),
(15, '2021-10-12 01:56:26.301566', '6', 'Guajira', 1, '[{\"added\": {}}]', 16, 1),
(16, '2021-10-12 01:56:37.855942', '1', 'Ciego', 1, '[{\"added\": {}}]', 22, 1),
(17, '2021-10-12 01:56:41.315000', '2', 'Sordo', 1, '[{\"added\": {}}]', 22, 1),
(18, '2021-10-12 01:56:52.028354', '3', 'Invalido de piernas', 1, '[{\"added\": {}}]', 22, 1),
(19, '2021-10-12 01:57:06.517553', '1', 'Retraso mental', 1, '[{\"added\": {}}]', 23, 1),
(20, '2021-10-12 01:57:13.771662', '2', 'Sindrome de Down', 1, '[{\"added\": {}}]', 23, 1),
(21, '2021-10-12 01:57:20.670680', '3', 'Esquizofrenia', 1, '[{\"added\": {}}]', 23, 1),
(22, '2021-10-12 01:57:31.919628', '1', 'Primaria', 1, '[{\"added\": {}}]', 12, 1),
(23, '2021-10-12 01:57:38.480542', '2', 'Secundaria', 1, '[{\"added\": {}}]', 12, 1),
(24, '2021-10-12 01:57:43.339289', '3', 'Kinder', 1, '[{\"added\": {}}]', 12, 1),
(25, '2021-10-12 01:58:06.196760', '4', 'Universidad', 1, '[{\"added\": {}}]', 12, 1),
(26, '2021-10-12 01:58:22.438659', '1', 'Asma', 1, '[{\"added\": {}}]', 24, 1),
(27, '2021-10-12 01:58:39.089751', '1', 'Exploradores', 1, '[{\"added\": {}}]', 13, 1),
(28, '2021-10-12 01:58:44.122728', '2', 'Semillas del Reino', 1, '[{\"added\": {}}]', 13, 1),
(29, '2021-10-12 01:58:51.698583', '1', 'Aplaudir', 1, '[{\"added\": {}}]', 18, 1),
(30, '2021-10-12 01:58:54.472614', '2', 'Bailar', 1, '[{\"added\": {}}]', 18, 1),
(31, '2021-10-12 01:58:57.185519', '3', 'Escuchar cuentos', 1, '[{\"added\": {}}]', 18, 1),
(32, '2021-10-12 01:59:03.332439', '4', 'Cantar', 1, '[{\"added\": {}}]', 18, 1),
(33, '2021-10-12 01:59:14.513587', '1', 'Arte', 1, '[{\"added\": {}}]', 19, 1),
(34, '2021-10-12 01:59:17.130483', '2', 'Musica', 1, '[{\"added\": {}}]', 19, 1),
(35, '2021-10-12 01:59:20.152584', '3', 'Matematicas', 1, '[{\"added\": {}}]', 19, 1),
(36, '2021-10-12 01:59:26.902372', '1', 'Catolica', 1, '[{\"added\": {}}]', 9, 1),
(37, '2021-10-12 01:59:30.180569', '2', 'Cristiana', 1, '[{\"added\": {}}]', 9, 1),
(38, '2021-10-12 01:59:32.877619', '3', 'Judia', 1, '[{\"added\": {}}]', 9, 1),
(39, '2021-10-12 01:59:35.453564', '4', 'Induismo', 1, '[{\"added\": {}}]', 9, 1),
(40, '2021-10-12 01:59:38.188585', '5', 'Budismo', 1, '[{\"added\": {}}]', 9, 1),
(41, '2021-10-12 01:59:41.008590', '6', 'Protestante', 1, '[{\"added\": {}}]', 9, 1),
(42, '2021-10-12 01:59:54.848893', '7', 'Indu', 1, '[{\"added\": {}}]', 9, 1),
(43, '2021-10-12 02:01:00.684650', '1', 'Masculino', 1, '[{\"added\": {}}]', 10, 1),
(44, '2021-10-12 02:01:05.607482', '2', 'Femenino', 1, '[{\"added\": {}}]', 10, 1),
(45, '2021-10-12 02:02:58.782635', '1', 'Debajo del Promedio', 1, '[{\"added\": {}}]', 11, 1),
(46, '2021-10-12 02:03:02.101597', '2', 'Promedio', 1, '[{\"added\": {}}]', 11, 1),
(47, '2021-10-12 02:03:05.222468', '3', 'Arriba del promedio', 1, '[{\"added\": {}}]', 11, 1),
(48, '2021-10-12 02:03:17.682456', '1', 'Escuela dominical', 1, '[{\"added\": {}}]', 14, 1),
(49, '2021-10-12 02:03:20.714571', '2', 'Grupo de danzas', 1, '[{\"added\": {}}]', 14, 1),
(50, '2021-10-12 02:03:23.246517', '3', 'Grupo de oración', 1, '[{\"added\": {}}]', 14, 1),
(51, '2021-10-12 02:06:58.803592', '4', 'Escuela dominical', 1, '[{\"added\": {}}]', 14, 1),
(52, '2021-10-12 02:07:02.350608', '5', 'Grupo de danzas', 1, '[{\"added\": {}}]', 14, 1),
(53, '2021-10-12 02:07:05.406358', '6', 'Grupo de oración', 1, '[{\"added\": {}}]', 14, 1),
(54, '2021-10-14 00:06:38.097954', '1', 'DEPORTIVO', 1, '[{\"added\": {}}]', 7, 1),
(55, '2021-10-14 00:07:12.544947', '2', 'Fisica', 1, '[{\"added\": {}}]', 7, 1),
(56, '2021-10-14 00:07:18.521060', '3', 'Cognitiva', 1, '[{\"added\": {}}]', 7, 1),
(57, '2021-10-14 00:07:27.757155', '4', 'Emocional', 1, '[{\"added\": {}}]', 7, 1),
(58, '2021-10-14 00:07:32.897097', '5', 'Social', 1, '[{\"added\": {}}]', 7, 1),
(59, '2021-10-14 00:08:21.496804', '1', 'Nuevo Post de muestra', 1, '[{\"added\": {}}]', 8, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(7, 'blog', 'categoria'),
(8, 'blog', 'post'),
(5, 'contenttypes', 'contenttype'),
(14, 'plantillas', 'actividadescristianas'),
(17, 'plantillas', 'beneficiario'),
(15, 'plantillas', 'ciudades'),
(20, 'plantillas', 'deberes'),
(16, 'plantillas', 'departamento'),
(22, 'plantillas', 'discapacidadesfisicas'),
(23, 'plantillas', 'discapacidadesmentales'),
(12, 'plantillas', 'educacionformal'),
(24, 'plantillas', 'enfermedadcronica'),
(13, 'plantillas', 'grupoetareo'),
(21, 'plantillas', 'historiaclinica'),
(18, 'plantillas', 'hobbies'),
(19, 'plantillas', 'materias'),
(9, 'plantillas', 'religion'),
(11, 'plantillas', 'rendimientoacademico'),
(10, 'plantillas', 'sexo'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2021-10-12 01:49:23.775465'),
(2, 'auth', '0001_initial', '2021-10-12 01:49:32.316364'),
(3, 'admin', '0001_initial', '2021-10-12 01:49:35.287665'),
(4, 'admin', '0002_logentry_remove_auto_add', '2021-10-12 01:49:35.336635'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2021-10-12 01:49:35.410592'),
(6, 'contenttypes', '0002_remove_content_type_name', '2021-10-12 01:49:36.044230'),
(7, 'auth', '0002_alter_permission_name_max_length', '2021-10-12 01:49:36.647884'),
(8, 'auth', '0003_alter_user_email_max_length', '2021-10-12 01:49:36.760820'),
(9, 'auth', '0004_alter_user_username_opts', '2021-10-12 01:49:36.847769'),
(10, 'auth', '0005_alter_user_last_login_null', '2021-10-12 01:49:37.643314'),
(11, 'auth', '0006_require_contenttypes_0002', '2021-10-12 01:49:37.695284'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2021-10-12 01:49:37.770244'),
(13, 'auth', '0008_alter_user_username_max_length', '2021-10-12 01:49:38.157338'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2021-10-12 01:49:38.319244'),
(15, 'auth', '0010_alter_group_name_max_length', '2021-10-12 01:49:38.477154'),
(16, 'auth', '0011_update_proxy_permissions', '2021-10-12 01:49:38.569101'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2021-10-12 01:49:38.772985'),
(18, 'blog', '0001_initial', '2021-10-12 01:49:42.249994'),
(19, 'sessions', '0001_initial', '2021-10-12 01:49:42.685745'),
(20, 'plantillas', '0001_initial', '2021-10-12 01:52:59.501269');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('4b69cth2tgm65z1jq4jpgtj4sx0zd2x4', '.eJxVjMsOwiAQAP-FsyE8FhSP3vsNZGEXqRqalPZk_HdD0oNeZybzFhH3rca98xpnElehxemXJcxPbkPQA9t9kXlp2zonORJ52C6nhfh1O9q_QcVex9YUNBdI7DSDA22D4QLpjAYsA3ltjfdMWaFhBZ6DzpZK8oEdISglPl_VXje7:1mfBYZ:j9I3NTpvbvT-3x_Up_Z7o36DbxwUPBsp8zI9vBvhZTc', '2021-11-09 01:47:15.076599'),
('csudtj2qz07vy85i0okqu23dnvpsjcb1', '.eJxVjMsOwiAQAP-FsyE8FhSP3vsNZGEXqRqalPZk_HdD0oNeZybzFhH3rca98xpnElehxemXJcxPbkPQA9t9kXlp2zonORJ52C6nhfh1O9q_QcVex9YUNBdI7DSDA22D4QLpjAYsA3ltjfdMWaFhBZ6DzpZK8oEdISglPl_VXje7:1mcTyA:9eX9HaPJ9EO4wTXeXnzcqvOaHCLdguqV9Kv98WqdkuU', '2021-11-01 14:50:30.360858');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `educacionformal`
--

CREATE TABLE `educacionformal` (
  `eformal_id` int(11) NOT NULL,
  `eformal_nombre` varchar(100) NOT NULL,
  `eformal_descripcion` longtext DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `educacionformal`
--

INSERT INTO `educacionformal` (`eformal_id`, `eformal_nombre`, `eformal_descripcion`) VALUES
(1, 'Primaria', ''),
(2, 'Secundaria', ''),
(3, 'Kinder', ''),
(4, 'Universidad', '');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `enfermedadcronica`
--

CREATE TABLE `enfermedadcronica` (
  `id` bigint(20) NOT NULL,
  `enfcronica_nombre` varchar(100) NOT NULL,
  `enfcronica_descripcion` longtext DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `enfermedadcronica`
--

INSERT INTO `enfermedadcronica` (`id`, `enfcronica_nombre`, `enfcronica_descripcion`) VALUES
(1, 'Asma', '');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `grupoetareo`
--

CREATE TABLE `grupoetareo` (
  `grupeta_id` int(11) NOT NULL,
  `grupeta_nombre` varchar(100) NOT NULL,
  `grupeta_descripcion` longtext DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `grupoetareo`
--

INSERT INTO `grupoetareo` (`grupeta_id`, `grupeta_nombre`, `grupeta_descripcion`) VALUES
(1, 'Exploradores', ''),
(2, 'Semillas del Reino', '');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `historiaclinica`
--

CREATE TABLE `historiaclinica` (
  `id` bigint(20) NOT NULL,
  `histclinica_peso` double DEFAULT NULL,
  `histclinica_talla` double DEFAULT NULL,
  `histclinica_tratMedico` longtext DEFAULT NULL,
  `histclinica_created` datetime(6) NOT NULL,
  `histclinica_updated` datetime(6) NOT NULL,
  `histclinica_beneid` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `historiaclinica`
--

INSERT INTO `historiaclinica` (`id`, `histclinica_peso`, `histclinica_talla`, `histclinica_tratMedico`, `histclinica_created`, `histclinica_updated`, `histclinica_beneid`) VALUES
(1, 10.15, 1.65, 'Dieta rica en carbohidratos', '2021-10-12 02:10:59.063152', '2021-10-12 02:10:59.063152', '30506040'),
(2, 55, 1.25, 'DIETA, ESTA MUY GORDO', '2021-10-13 00:42:13.622957', '2021-10-13 00:42:13.622957', '6030908010');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `historiaclinica_histclinica_disfisica`
--

CREATE TABLE `historiaclinica_histclinica_disfisica` (
  `id` int(11) NOT NULL,
  `historiaclinica_id` bigint(20) NOT NULL,
  `discapacidadesfisicas_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `historiaclinica_histclinica_disfisica`
--

INSERT INTO `historiaclinica_histclinica_disfisica` (`id`, `historiaclinica_id`, `discapacidadesfisicas_id`) VALUES
(1, 1, 3),
(2, 2, 3);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `historiaclinica_histclinica_dismental`
--

CREATE TABLE `historiaclinica_histclinica_dismental` (
  `id` int(11) NOT NULL,
  `historiaclinica_id` bigint(20) NOT NULL,
  `discapacidadesmentales_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `historiaclinica_histclinica_dismental`
--

INSERT INTO `historiaclinica_histclinica_dismental` (`id`, `historiaclinica_id`, `discapacidadesmentales_id`) VALUES
(1, 1, 2),
(2, 2, 3);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `historiaclinica_histclinica_enfcronica`
--

CREATE TABLE `historiaclinica_histclinica_enfcronica` (
  `id` int(11) NOT NULL,
  `historiaclinica_id` bigint(20) NOT NULL,
  `enfermedadcronica_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `historiaclinica_histclinica_enfcronica`
--

INSERT INTO `historiaclinica_histclinica_enfcronica` (`id`, `historiaclinica_id`, `enfermedadcronica_id`) VALUES
(1, 1, 1),
(2, 2, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `hobbies`
--

CREATE TABLE `hobbies` (
  `hob_id` int(11) NOT NULL,
  `hob_nombre` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `hobbies`
--

INSERT INTO `hobbies` (`hob_id`, `hob_nombre`) VALUES
(1, 'Aplaudir'),
(2, 'Bailar'),
(3, 'Escuchar cuentos'),
(4, 'Cantar');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `materias`
--

CREATE TABLE `materias` (
  `mat_id` int(11) NOT NULL,
  `mat_nombre` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `materias`
--

INSERT INTO `materias` (`mat_id`, `mat_nombre`) VALUES
(1, 'Arte'),
(2, 'Musica'),
(3, 'Matematicas');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `religion`
--

CREATE TABLE `religion` (
  `rel_id` int(11) NOT NULL,
  `rel_nombre` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `religion`
--

INSERT INTO `religion` (`rel_id`, `rel_nombre`) VALUES
(1, 'Catolica'),
(2, 'Cristiana'),
(3, 'Judia'),
(4, 'Induismo'),
(5, 'Budismo'),
(6, 'Protestante'),
(7, 'Indu');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `rendimientoacademico`
--

CREATE TABLE `rendimientoacademico` (
  `rendiaca_id` int(11) NOT NULL,
  `rendiaca_nombre` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `rendimientoacademico`
--

INSERT INTO `rendimientoacademico` (`rendiaca_id`, `rendiaca_nombre`) VALUES
(1, 'Debajo del Promedio'),
(2, 'Promedio'),
(3, 'Arriba del promedio');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `sexo`
--

CREATE TABLE `sexo` (
  `sex_id` int(11) NOT NULL,
  `sex_nombre` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `sexo`
--

INSERT INTO `sexo` (`sex_id`, `sex_nombre`) VALUES
(1, 'Masculino'),
(2, 'Femenino');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `actividadescristianas`
--
ALTER TABLE `actividadescristianas`
  ADD PRIMARY KEY (`activcris_id`);

--
-- Indices de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indices de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indices de la tabla `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indices de la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indices de la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `beneficiario`
--
ALTER TABLE `beneficiario`
  ADD PRIMARY KEY (`benef_id`),
  ADD KEY `beneficiario_benef_ciudad_c32a7bf6_fk_ciudades_ciu_id` (`benef_ciudad`),
  ADD KEY `beneficiario_benef_departamento_f0cd2f52_fk_departamento_dep_id` (`benef_departamento`),
  ADD KEY `beneficiario_benef_eduformal_2c103bb2_fk_educacion` (`benef_eduformal`),
  ADD KEY `beneficiario_benef_grupoeta_65ee7acc_fk_grupoetareo_grupeta_id` (`benef_grupoeta`),
  ADD KEY `beneficiario_benef_religion_95292e4e_fk_religion_rel_id` (`benef_religion`),
  ADD KEY `beneficiario_benef_rendiaca_a1cd7f31_fk_rendimien` (`benef_rendiaca`),
  ADD KEY `beneficiario_benef_sexo_dfca4d7a_fk_sexo_sex_id` (`benef_sexo`),
  ADD KEY `beneficiario_benef_activcrist_ea2422d6_fk_actividad` (`benef_activcrist`);

--
-- Indices de la tabla `beneficiario_benef_deberes`
--
ALTER TABLE `beneficiario_benef_deberes`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `beneficiario_benef_deber_beneficiario_id_deberes__de417e41_uniq` (`beneficiario_id`,`deberes_id`),
  ADD KEY `beneficiario_benef_deberes_deberes_id_860415f5_fk_deberes_deb_id` (`deberes_id`);

--
-- Indices de la tabla `beneficiario_benef_hobbies`
--
ALTER TABLE `beneficiario_benef_hobbies`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `beneficiario_benef_hobbi_beneficiario_id_hobbies__2926024d_uniq` (`beneficiario_id`,`hobbies_id`),
  ADD KEY `beneficiario_benef_hobbies_hobbies_id_6666a04f_fk_hobbies_hob_id` (`hobbies_id`);

--
-- Indices de la tabla `beneficiario_benef_materias`
--
ALTER TABLE `beneficiario_benef_materias`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `beneficiario_benef_mater_beneficiario_id_materias_0d7562f3_uniq` (`beneficiario_id`,`materias_id`),
  ADD KEY `beneficiario_benef_m_materias_id_1918b6b8_fk_materias_` (`materias_id`);

--
-- Indices de la tabla `blog_categoria`
--
ALTER TABLE `blog_categoria`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `blog_post`
--
ALTER TABLE `blog_post`
  ADD PRIMARY KEY (`id`),
  ADD KEY `blog_post_autor_id_8811ea21_fk_auth_user_id` (`autor_id`);

--
-- Indices de la tabla `blog_post_categorias`
--
ALTER TABLE `blog_post_categorias`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `blog_post_categorias_post_id_categoria_id_70b54e48_uniq` (`post_id`,`categoria_id`),
  ADD KEY `blog_post_categorias_categoria_id_f3743c06_fk_blog_categoria_id` (`categoria_id`);

--
-- Indices de la tabla `ciudades`
--
ALTER TABLE `ciudades`
  ADD PRIMARY KEY (`ciu_id`);

--
-- Indices de la tabla `deberes`
--
ALTER TABLE `deberes`
  ADD PRIMARY KEY (`deb_id`);

--
-- Indices de la tabla `departamento`
--
ALTER TABLE `departamento`
  ADD PRIMARY KEY (`dep_id`);

--
-- Indices de la tabla `discapacidadesfisicas`
--
ALTER TABLE `discapacidadesfisicas`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `discapacidadesmentales`
--
ALTER TABLE `discapacidadesmentales`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indices de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indices de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indices de la tabla `educacionformal`
--
ALTER TABLE `educacionformal`
  ADD PRIMARY KEY (`eformal_id`);

--
-- Indices de la tabla `enfermedadcronica`
--
ALTER TABLE `enfermedadcronica`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `grupoetareo`
--
ALTER TABLE `grupoetareo`
  ADD PRIMARY KEY (`grupeta_id`);

--
-- Indices de la tabla `historiaclinica`
--
ALTER TABLE `historiaclinica`
  ADD PRIMARY KEY (`id`),
  ADD KEY `historiaclinica_histclinica_beneid_a94283e6_fk_beneficia` (`histclinica_beneid`);

--
-- Indices de la tabla `historiaclinica_histclinica_disfisica`
--
ALTER TABLE `historiaclinica_histclinica_disfisica`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `historiaclinica_histclin_historiaclinica_id_disca_41c430c0_uniq` (`historiaclinica_id`,`discapacidadesfisicas_id`),
  ADD KEY `historiaclinica_hist_discapacidadesfisica_8a884248_fk_discapaci` (`discapacidadesfisicas_id`);

--
-- Indices de la tabla `historiaclinica_histclinica_dismental`
--
ALTER TABLE `historiaclinica_histclinica_dismental`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `historiaclinica_histclin_historiaclinica_id_disca_8966370e_uniq` (`historiaclinica_id`,`discapacidadesmentales_id`),
  ADD KEY `historiaclinica_hist_discapacidadesmental_ae4d9f80_fk_discapaci` (`discapacidadesmentales_id`);

--
-- Indices de la tabla `historiaclinica_histclinica_enfcronica`
--
ALTER TABLE `historiaclinica_histclinica_enfcronica`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `historiaclinica_histclin_historiaclinica_id_enfer_e866097d_uniq` (`historiaclinica_id`,`enfermedadcronica_id`),
  ADD KEY `historiaclinica_hist_enfermedadcronica_id_fefb0ac9_fk_enfermeda` (`enfermedadcronica_id`);

--
-- Indices de la tabla `hobbies`
--
ALTER TABLE `hobbies`
  ADD PRIMARY KEY (`hob_id`);

--
-- Indices de la tabla `materias`
--
ALTER TABLE `materias`
  ADD PRIMARY KEY (`mat_id`);

--
-- Indices de la tabla `religion`
--
ALTER TABLE `religion`
  ADD PRIMARY KEY (`rel_id`);

--
-- Indices de la tabla `rendimientoacademico`
--
ALTER TABLE `rendimientoacademico`
  ADD PRIMARY KEY (`rendiaca_id`);

--
-- Indices de la tabla `sexo`
--
ALTER TABLE `sexo`
  ADD PRIMARY KEY (`sex_id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `actividadescristianas`
--
ALTER TABLE `actividadescristianas`
  MODIFY `activcris_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=97;

--
-- AUTO_INCREMENT de la tabla `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `beneficiario_benef_deberes`
--
ALTER TABLE `beneficiario_benef_deberes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `beneficiario_benef_hobbies`
--
ALTER TABLE `beneficiario_benef_hobbies`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `beneficiario_benef_materias`
--
ALTER TABLE `beneficiario_benef_materias`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `blog_categoria`
--
ALTER TABLE `blog_categoria`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `blog_post`
--
ALTER TABLE `blog_post`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `blog_post_categorias`
--
ALTER TABLE `blog_post_categorias`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `ciudades`
--
ALTER TABLE `ciudades`
  MODIFY `ciu_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `deberes`
--
ALTER TABLE `deberes`
  MODIFY `deb_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `departamento`
--
ALTER TABLE `departamento`
  MODIFY `dep_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `discapacidadesfisicas`
--
ALTER TABLE `discapacidadesfisicas`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `discapacidadesmentales`
--
ALTER TABLE `discapacidadesmentales`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=60;

--
-- AUTO_INCREMENT de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT de la tabla `enfermedadcronica`
--
ALTER TABLE `enfermedadcronica`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `historiaclinica`
--
ALTER TABLE `historiaclinica`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `historiaclinica_histclinica_disfisica`
--
ALTER TABLE `historiaclinica_histclinica_disfisica`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `historiaclinica_histclinica_dismental`
--
ALTER TABLE `historiaclinica_histclinica_dismental`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `historiaclinica_histclinica_enfcronica`
--
ALTER TABLE `historiaclinica_histclinica_enfcronica`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `hobbies`
--
ALTER TABLE `hobbies`
  MODIFY `hob_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `materias`
--
ALTER TABLE `materias`
  MODIFY `mat_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `religion`
--
ALTER TABLE `religion`
  MODIFY `rel_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de la tabla `rendimientoacademico`
--
ALTER TABLE `rendimientoacademico`
  MODIFY `rendiaca_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `sexo`
--
ALTER TABLE `sexo`
  MODIFY `sex_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Filtros para la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Filtros para la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `beneficiario`
--
ALTER TABLE `beneficiario`
  ADD CONSTRAINT `beneficiario_benef_activcrist_ea2422d6_fk_actividad` FOREIGN KEY (`benef_activcrist`) REFERENCES `actividadescristianas` (`activcris_id`),
  ADD CONSTRAINT `beneficiario_benef_ciudad_c32a7bf6_fk_ciudades_ciu_id` FOREIGN KEY (`benef_ciudad`) REFERENCES `ciudades` (`ciu_id`),
  ADD CONSTRAINT `beneficiario_benef_departamento_f0cd2f52_fk_departamento_dep_id` FOREIGN KEY (`benef_departamento`) REFERENCES `departamento` (`dep_id`),
  ADD CONSTRAINT `beneficiario_benef_eduformal_2c103bb2_fk_educacion` FOREIGN KEY (`benef_eduformal`) REFERENCES `educacionformal` (`eformal_id`),
  ADD CONSTRAINT `beneficiario_benef_grupoeta_65ee7acc_fk_grupoetareo_grupeta_id` FOREIGN KEY (`benef_grupoeta`) REFERENCES `grupoetareo` (`grupeta_id`),
  ADD CONSTRAINT `beneficiario_benef_religion_95292e4e_fk_religion_rel_id` FOREIGN KEY (`benef_religion`) REFERENCES `religion` (`rel_id`),
  ADD CONSTRAINT `beneficiario_benef_rendiaca_a1cd7f31_fk_rendimien` FOREIGN KEY (`benef_rendiaca`) REFERENCES `rendimientoacademico` (`rendiaca_id`),
  ADD CONSTRAINT `beneficiario_benef_sexo_dfca4d7a_fk_sexo_sex_id` FOREIGN KEY (`benef_sexo`) REFERENCES `sexo` (`sex_id`);

--
-- Filtros para la tabla `beneficiario_benef_deberes`
--
ALTER TABLE `beneficiario_benef_deberes`
  ADD CONSTRAINT `beneficiario_benef_d_beneficiario_id_4cb69dd7_fk_beneficia` FOREIGN KEY (`beneficiario_id`) REFERENCES `beneficiario` (`benef_id`),
  ADD CONSTRAINT `beneficiario_benef_deberes_deberes_id_860415f5_fk_deberes_deb_id` FOREIGN KEY (`deberes_id`) REFERENCES `deberes` (`deb_id`);

--
-- Filtros para la tabla `beneficiario_benef_hobbies`
--
ALTER TABLE `beneficiario_benef_hobbies`
  ADD CONSTRAINT `beneficiario_benef_h_beneficiario_id_cd963c6c_fk_beneficia` FOREIGN KEY (`beneficiario_id`) REFERENCES `beneficiario` (`benef_id`),
  ADD CONSTRAINT `beneficiario_benef_hobbies_hobbies_id_6666a04f_fk_hobbies_hob_id` FOREIGN KEY (`hobbies_id`) REFERENCES `hobbies` (`hob_id`);

--
-- Filtros para la tabla `beneficiario_benef_materias`
--
ALTER TABLE `beneficiario_benef_materias`
  ADD CONSTRAINT `beneficiario_benef_m_beneficiario_id_fa779f47_fk_beneficia` FOREIGN KEY (`beneficiario_id`) REFERENCES `beneficiario` (`benef_id`),
  ADD CONSTRAINT `beneficiario_benef_m_materias_id_1918b6b8_fk_materias_` FOREIGN KEY (`materias_id`) REFERENCES `materias` (`mat_id`);

--
-- Filtros para la tabla `blog_post`
--
ALTER TABLE `blog_post`
  ADD CONSTRAINT `blog_post_autor_id_8811ea21_fk_auth_user_id` FOREIGN KEY (`autor_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `blog_post_categorias`
--
ALTER TABLE `blog_post_categorias`
  ADD CONSTRAINT `blog_post_categorias_categoria_id_f3743c06_fk_blog_categoria_id` FOREIGN KEY (`categoria_id`) REFERENCES `blog_categoria` (`id`),
  ADD CONSTRAINT `blog_post_categorias_post_id_212bf44c_fk_blog_post_id` FOREIGN KEY (`post_id`) REFERENCES `blog_post` (`id`);

--
-- Filtros para la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `historiaclinica`
--
ALTER TABLE `historiaclinica`
  ADD CONSTRAINT `historiaclinica_histclinica_beneid_a94283e6_fk_beneficia` FOREIGN KEY (`histclinica_beneid`) REFERENCES `beneficiario` (`benef_id`);

--
-- Filtros para la tabla `historiaclinica_histclinica_disfisica`
--
ALTER TABLE `historiaclinica_histclinica_disfisica`
  ADD CONSTRAINT `historiaclinica_hist_discapacidadesfisica_8a884248_fk_discapaci` FOREIGN KEY (`discapacidadesfisicas_id`) REFERENCES `discapacidadesfisicas` (`id`),
  ADD CONSTRAINT `historiaclinica_hist_historiaclinica_id_2e1c246f_fk_historiac` FOREIGN KEY (`historiaclinica_id`) REFERENCES `historiaclinica` (`id`);

--
-- Filtros para la tabla `historiaclinica_histclinica_dismental`
--
ALTER TABLE `historiaclinica_histclinica_dismental`
  ADD CONSTRAINT `historiaclinica_hist_discapacidadesmental_ae4d9f80_fk_discapaci` FOREIGN KEY (`discapacidadesmentales_id`) REFERENCES `discapacidadesmentales` (`id`),
  ADD CONSTRAINT `historiaclinica_hist_historiaclinica_id_05d1033c_fk_historiac` FOREIGN KEY (`historiaclinica_id`) REFERENCES `historiaclinica` (`id`);

--
-- Filtros para la tabla `historiaclinica_histclinica_enfcronica`
--
ALTER TABLE `historiaclinica_histclinica_enfcronica`
  ADD CONSTRAINT `historiaclinica_hist_enfermedadcronica_id_fefb0ac9_fk_enfermeda` FOREIGN KEY (`enfermedadcronica_id`) REFERENCES `enfermedadcronica` (`id`),
  ADD CONSTRAINT `historiaclinica_hist_historiaclinica_id_9574b548_fk_historiac` FOREIGN KEY (`historiaclinica_id`) REFERENCES `historiaclinica` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
