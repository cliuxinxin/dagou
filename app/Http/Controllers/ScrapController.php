<?php

namespace App\Http\Controllers;

use App\Scrap;
use Illuminate\Http\Request;

class ScrapController extends Controller
{
    //
    public function index()
    {
        $items = Scrap::paginate(20);

        return view('scrape',compact('items'));
    }

}
