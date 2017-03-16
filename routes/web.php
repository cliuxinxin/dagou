<?php

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/

Route::get('/', 'ItemsController@index');

Auth::routes();

Route::get('/home', 'HomeController@index');

Route::get('/scrape', 'ScrapController@index')->name('scrape');

Route::get('/hospital', 'ItemsController@hospital')->name('hospital');

Route::get('/group', 'GroupsController@index')->name('group');