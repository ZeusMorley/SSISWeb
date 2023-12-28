CREATE TABLE IF NOT EXISTS college (
    id INT AUTO_INCREMENT PRIMARY KEY,
    collegeCode VARCHAR(8) UNIQUE NOT NULL,
    collegeName VARCHAR(128) UNIQUE NOT NULL,
);

CREATE TABLE IF NOT EXISTS course (
    id INT AUTO_INCREMENT PRIMARY KEY,
    courseCode VARCHAR(8) UNIQUE NOT NULL,
    courseName VARCHAR(128) UNIQUE NOT NULL,
    collegeId INT,
    FOREIGN KEY (collegeId) REFERENCES college(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS student (
    id INT AUTO_INCREMENT PRIMARY KEY,
    studentId VARCHAR(16) UNIQUE NOT NULL,
    firstName VARCHAR(64) NOT NULL,
    lastName VARCHAR(32) NOT NULL,
    gender VARCHAR(8) NOT NULL,
    year INT NOT NULL,
    courseId INT,
    FOREIGN KEY (courseId) REFERENCES course(id) ON DELETE CASCADE,
    cloudinary_url VARCHAR(255)
);