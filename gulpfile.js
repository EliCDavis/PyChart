
var gulp       = require('gulp');
var uglify     = require("gulp-uglify");
var concat     = require('gulp-concat');

gulp.task('css', function () {

    gulp.src(['htmlDependencies/**/*.css'])
        .pipe(concat('style.css'))
        .pipe(gulp.dest('./src/'));

});

gulp.task('js', function () {

    gulp.src(['htmlDependencies/js/**/*.js'])
        .pipe(concat('script.js'))
        .pipe(gulp.dest('./src/'));

});

gulp.task('default', ['css', 'js'], function () {

    gulp.src(['htmlDependencies/**/*.css'])
        .pipe(concat('style.css'))
        .pipe(gulp.dest('./src/'));

});